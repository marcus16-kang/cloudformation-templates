# ElastiCache Multi AZ Cluster

## Parameters

### `ParameterGroupFamily`

- `redis`
  - `redis7`
  - `redis6.x`
  - `redis5.0`
  - `redis4.0`
  - `redis3.2`
  - `redis2.8`
  - `redis2.6`
- `memcached`
  - `memcached1.6`
  - `memcached1.5`
  - `memcached1.4`

### `AutoMinorVersionUpgrade`

- `true` (default)
- `false`

### `CacheNodeType`

[Amazon ElastiCache Instance Types](https://aws.amazon.com/ko/elasticache/pricing/)

### `Engine` and `EngineVersion`

- `redis` (default)
  - `7.0` (default)
  - `6.2`
  - `6.0`
  - `5.0.6`
  - `5.0.5`
  - `5.0.4`
  - `5.0.3`
  - `5.0.0`
  - `4.0.10`
  - `3.2.6`
  - `3.2.4`
  - `3.2.10`
  - `2.8.6`
  - `2.8.24`
  - `2.8.23`
  - `2.8.22`
  - `2.8.21`
  - `2.8.19`
  - `2.6.13`
- `memcached`
  - `1.6.6`
  - `1.6.12`
  - `1.5.16`
  - `1.5.10`
  - `1.4.5`
  - `1.4.34`
  - `1.4.33`
  - `1.4.24`
  - `1.4.14`

### `IpDiscovery`

- `ipv4` (default)
- `ipv6`

### `NetworkType`

- `ipv4` (default)
- `ipv6`
- `dual_stack`


### `TransitEncryptionEnabled`

- `false` (default)
- `true`

**Note**

If you enable transit encryption, the default mode is `Required`. It means that **TLS** is essential to connecting Redis.

So, when you want to connect Redis using TCP that be enabled transit encryption, you should change `Required` to `Preferred` at console or CLI.


## Scripts

### Linux

``` bash
### Common Parameters - ElastiCache Informations
PARAMETER_GROUP_FAMILY="<cache parameter group family>"
PARAMETER_GROUP_NAME="<cache parameter group name>"
SUBNET_GROUP_NAME="<cache subnet group name>"
# AUTO_MINOR_VERSION_UPGRADE="<cache auto minor version update>"
CACHE_NODE_TYPE="<cache instance class>"
REPLICATION_GROUP_ID="<cache cluster name>"
# TRANSIT_ENCRYPTION_ENABLED="<cache cluster transit encryption>"
KMS_KEY_ID="<cache cluster encryption kms key arn>"
# REPLICAS_PER_NODE_GROUP="<cache cluster replicas per node group>"

### Common Parameters - Network Informations
# NETWORK_TYPE="<cache network type>"
# IP_DISCOVERY="<cache ip discovery type>"
SUBNETS="<subnet ids with comma>"
SECURITY_GROUP_NAME="<cache security group name>"
VPC_ID="<vpc id>"

### Common Parameters - ElastiCache Informations
ENGINE="<database engine>"
ENGINE_VERSION="<database engine version>"
PORT="<database port>"  # Redis: 6379, Memcached: 11211

### Common Parameters - Log Informations
# SLOW_LOG_DESTINATION_NAME="<slow log's log group name>"
# ENGINE_LOG_DESTINATION_NAME="<slow log's log gruop name>"

### CloudFormation Parameters
STACK_NAME="<cloudformation stack name>"
REGION="<cloudformation region code>"


aws cloudformation deploy \
    --stack-name $STACK_NAME \
    --template-file ./cluster.yaml \
    --parameter-overrides \
        ParameterGroupFamily=$PARAMETER_GROUP_FAMILY \
        ParameterGroupName=$PARAMETER_GROUP_NAME \
        SubnetGroupName=$SUBNET_GROUP_NAME \
        SubnetIds=$SUBNETS \
        VpcId=$VPC_ID \
        SecurityGroupName=$SECURITY_GROUP_NAME \
        # AutoMinorVersionUpgrade=$AUTO_MINOR_VERSION_UPGRADE \
        CacheNodeType=$CACHE_NODE_TYPE \
        Engine=$ENGINE \
        EngineVersion=$ENGINE_VERSION \
        # IpDiscovery=$IP_DISCOVERY \
        KmsKeyId=$KMS_KEY_ID \
        # SlowLogDestinationName=$SLOW_LOG_DESTINATION_NAME \
        # EngineLogDestinationName=$ENGINE_LOG_DESTINATION_NAME \
        # NetworkType=$NETWORK_TYPE \
        Port=$PORT \
        # ReplicasPerNodeGroup=$REPLICAS_PER_NODE_GROUP \
        ReplicationGroupId=$REPLICATION_GROUP_ID \
        # TransitEncryptionEnabled=$TRANSIT_ENCRYPTION_ENABLED \
    --region $REGION
```

### Windows

``` powershell
### Common Parameters - ElastiCache Informations
$PARAMETER_GROUP_FAMILY="<cache parameter group family>"
$PARAMETER_GROUP_NAME="<cache parameter group name>"
$SUBNET_GROUP_NAME="<cache subnet group name>"
# $AUTO_MINOR_VERSION_UPGRADE="<cache auto minor version update>"
$CACHE_NODE_TYPE="<cache instance class>"
$REPLICATION_GROUP_ID="<cache cluster name>"
# $TRANSIT_ENCRYPTION_ENABLED="<cache cluster transit encryption>"
$KMS_KEY_ID="<cache cluster encryption kms key arn>"
# $REPLICAS_PER_NODE_GROUP="<cache cluster replicas per node group>"

### Common Parameters - Network Informations
# $NETWORK_TYPE="<cache network type>"
# $IP_DISCOVERY="<cache ip discovery type>"
$SUBNETS="<subnet ids with comma>"
$SECURITY_GROUP_NAME="<cache security group name>"
$VPC_ID="<vpc id>"
$
### Common Parameters - ElastiCache Informations
$ENGINE="<database engine>"
$ENGINE_VERSION="<database engine version>"
$PORT="<database port>"  # Redis: 6379, Memcached: 11211

### Common Parameters - Log Informations
# $SLOW_LOG_DESTINATION_NAME="<slow log's log group name>"
# $ENGINE_LOG_DESTINATION_NAME="<slow log's log gruop name>"

### CloudFormation Parameters
$STACK_NAME="<cloudformation stack name>"
$REGION="<cloudformation region code>"


aws cloudformation deploy `
    --stack-name $STACK_NAME `
    --template-file ./cluster.yaml `
    --parameter-overrides `
        ParameterGroupFamily=$PARAMETER_GROUP_FAMILY `
        ParameterGroupName=$PARAMETER_GROUP_NAME `
        SubnetGroupName=$SUBNET_GROUP_NAME `
        SubnetIds=$SUBNETS `
        VpcId=$VPC_ID `
        SecurityGroupName=$SECURITY_GROUP_NAME `
        # AutoMinorVersionUpgrade=$AUTO_MINOR_VERSION_UPGRADE `
        CacheNodeType=$CACHE_NODE_TYPE `
        Engine=$ENGINE `
        EngineVersion=$ENGINE_VERSION `
        # IpDiscovery=$IP_DISCOVERY `
        KmsKeyId=$KMS_KEY_ID `
        # SlowLogDestinationName=$SLOW_LOG_DESTINATION_NAME `
        # EngineLogDestinationName=$ENGINE_LOG_DESTINATION_NAME `
        # NetworkType=$NETWORK_TYPE `
        Port=$PORT `
        # ReplicasPerNodeGroup=$REPLICAS_PER_NODE_GROUP `
        ReplicationGroupId=$REPLICATION_GROUP_ID `
        # TransitEncryptionEnabled=$TRANSIT_ENCRYPTION_ENABLED `
    --region $REGION
```