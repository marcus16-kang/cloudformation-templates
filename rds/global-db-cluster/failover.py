import os
import boto3
from botocore.config import Config
from datetime import datetime

def get_failover_to_cluster(global_cluster_name: str) -> str:
    client = boto3.client('rds')

    global_cluster_info = client.describe_global_clusters(
        GlobalClusterIdentifier=global_cluster_name
    )['GlobalClusters'][0]
    failover_state = global_cluster_info.get('FailoverState', None)

    if failover_state:
        cluster_arn = failover_state['ToDbClusterArn']
    
    else:
        cluster_arn = [item['DBClusterArn'] for item in global_cluster_info['GlobalClusterMembers'] if item.get('IsWriter', False)][0]
    
    return cluster_arn


def get_endpoint(cluster_arn: str) -> str:
    cluster_region = cluster_arn.split(':')[3]
    client = boto3.client('rds', config=Config(region_name=cluster_region))

    response = client.describe_db_clusters(
        DBClusterIdentifier=cluster_arn
    )
    endpoint = response['DBClusters'][0]['Endpoint']

    return endpoint

def update_route53_record(hosted_zone_id: str, record_name: str, endpoint: str) -> None:
    client = boto3.client('route53')

    client.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            'Comment': f'Database failover at {str(datetime.now())}',
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecoredSet': {
                        'Name': record_name,
                        'Type': 'CNAME',
                        'TTL': 30,
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
    # populate the existing environment information
    global_cluster_name = os.getenv('RDS_GLOBAL_CLUSTER_NAME', None)   # test only
    hosted_zone_id = os.getenv('ROUTE53_HOSTED_ZONE_ID', None)
    record_name = os.getenv('ROUTE53_RECORD_NAME', None)

    if global_cluster_name is None:
        print('Please set the environment variable "RDS_GLOBAL_CLUSTER_NAME".')
    
    if hosted_zone_id is None:
        print('Please set the environment variable "ROUTE53_HOSTED_ZONE_ID".')
    
    if record_name is None:
        print('Please set the environment variable "ROUTE53_RECORD_NAME".')
    
    if global_cluster_name is not None and hosted_zone_id is not None and record_name is not None:
        try:
            cluster_arn = get_failover_to_cluster(global_cluster_name)
            cluster_endpoint = get_endpoint(cluster_arn)
            update_route53_record(hosted_zone_id, record_name, cluster_endpoint)

        except Exception as e:
            print(e)
    
    else:
        return