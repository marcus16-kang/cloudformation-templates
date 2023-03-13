import os
import redis
from rediscluster import RedisCluster
import boto3
from datetime import datetime

def get_primary_cluster(global_datastore_name):
    try:
        client = boto3.client('elasticache')
        response = client.describe_global_replication_groups(
            GlobalReplicationGroupId=global_datastore_name,
            ShowMemberInfo=True
        )
        members = response['GlobalReplicationGroups'][0]['Members']
        primary_cluster = [item for item in members if item['Role'] == 'PRIMARY'][0]
        
        return primary_cluster
        
    except Exception as e:
        print(e.__str__())

def get_primary_cluster_endpoint(cluster_name: str, region: str, cluster: bool):
    try:
        client = boto3.session.Session(region_name=region).client('elasticache')
        response = client.describe_replication_groups(
            ReplicationGroupId=cluster_name
        )
        if cluster:
            endpoint = response['ReplicationGroups'][0]['ConfigurationEndpoint']['Address']
        
        else:
            endpoint = response['ReplicationGroups'][0]['NodeGroups'][0]['PrimaryEndpoint']['Address']
        
        return endpoint
    
    except Exception as e:
        print(e.__str_())

def change_route53_record_set(cache_hostname: str, hosted_zone_id: str, endpoint:str , ttl=10):
    client = boto3.client('route53')

    client.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            'Comment': f'Cache failover at {str(datetime.now())}',
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': cache_hostname,
                        'Type': 'CNAME',
                        'TTL': ttl,
                        'ResourceRecords': [
                            {
                                'Value': endpoint
                            }
                        ]
                    }
                }
            ]
        }
    )
    

def lambda_handler(event, context):
    global_datastore_name = os.getenv('ELASTICACHE_GLOBAL_DATASTORE_NAME', None)
    hosted_zone_id = os.getenv('ROUTE53_HOSTED_ZONE_ID', None)
    ttl = int(os.getenv('ROUTE53_TTL', '10'))
    cache_hostname = os.getenv('CACHE_HOSTNAME', None)
    cache_port = int(os.getenv('CACHE_PORT', '6379'))
    cache_cluster = True if os.getenv('CACHE_CLUSTER', False) else False
    cache_tls = True if os.getenv('CACHE_TLS', False) else False

    if global_datastore_name is None:
        print('Please set the environment variable "ELASTICACHE_GLOBAL_DATASTORE_NAME".')
    
    if hosted_zone_id is None:
        print('Please set the environment variable "ROUTE53_HOSTED_ZONE_ID".')
    
    if cache_hostname is None:
        print('Please set the environment variable "CACHE_HOSTNAME".')
    
    if global_datastore_name is not None and hosted_zone_id is not None and cache_hostname is not None:
        try:
            if cache_cluster:
                r = RedisCluster(startup_nodes=[{'host': cache_hostname, 'port': str(cache_port)}], decode_responses=True, skip_full_coverage_check=True, ssl=cache_tls, ssl_cert_reqs=None)

            else:
                r = redis.Redis(cache_hostname, port=cache_port, socket_connect_timeout=5, ssl=cache_tls, ssl_cert_reqs=None)
            
            r.set('ping', 'pong')
        
        except redis.exceptions.TimeoutError:
            print('timeout')
            
            primary_cluster = get_primary_cluster(global_datastore_name)
            endpoint = get_primary_cluster_endpoint(primary_cluster['ReplicationGroupId'], primary_cluster['ReplicationGroupRegion'], cluster=cache_cluster)
            change_route53_record_set(cache_hostname, hosted_zone_id, endpoint, ttl)
        
        except redis.exceptions.ReadOnlyError:
            print('readonly')
            
            primary_cluster = get_primary_cluster(global_datastore_name)
            endpoint = get_primary_cluster_endpoint(primary_cluster['ReplicationGroupId'], primary_cluster['ReplicationGroupRegion'], cluster=cache_cluster)
            change_route53_record_set(cache_hostname, hosted_zone_id, endpoint, ttl)
    
    else:
        return
