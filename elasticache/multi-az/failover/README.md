# Failover Automation for ElastiCache Global Datastore

## Create the Lambda layer

You should create a Lambda layer for Lambda function to use `redis-py` library.

Please download [ZIP file](https://github.com/marcus16-kang/cloudformation-templates/files/10953578/redis.zip) and create a layer.

``` shell
aws lambda publish-layer-version --layer-name <LAYER_NAME> --description <DESCRIPTION> --compatible-runtimes "python3.9" --compatible-architectures  "arm64" --zip-file fileb://redis.zip --region <REGION>
```

### Create the layer file

``` shell
mkdir python
pip3 install redis redis-py-cluster -t ./python
zip -r redis.zip ./python
```

## Deploy CloudFormation Stack

### Linux

``` bash
STACK_NAME=""
REGION=""

ProjectName=""                      # [REQUIRED] The name of this project.
ElastiCacheGlobalDatastoreName=""   # [REQUIRED] The name of ElastiCache global datastore.
Route53HostesdZoneId=""             # [REQUIRED] The id of Route53 Hosted Zone.
Route53RecoreTtl="10"               # [optional] The ttl value of Route53 record.
CacheHostname=""                    # [REQUIRED] The record name of Route53 Hosted Zone(ex. cache.test.lobal).
CachePort="6379"                    # [REQUIRED] The port number to access cache clusters.
CacheClusterEnabled="False"         # (False, True) [REQUIRED] Enable or disable Elasticache Cluster.
CacheTlsEnabled="False"             # (False, True) [REQUIRED] Enable or disable Elasticache TLS Encryption.
RoleName=""                         # [REQUIRED] The name of function's IAM role.
FunctionName=""                     # [REQUIRED] The name of Lambda function.
LayerVersionArn=""                  # [REQUIRED] The arn of Lambda layer with version.
SecurityGroupId=""                  # [REQUIRED] The ID of security group for Lambda function.
Subnets=""                          # [REQUIRED] The IDs of subnet for Lambda function.
EventName=""                        # [REQUIRED] The name of EventBridge rule.
EventInterval="5"                   # [REQUIRED] The number of interval time(minutes) to trigger EventBridge rule.

curl -O https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/elasticache/multi-az/failover/template.yaml

aws cloudformation deploy \
    --template-file template.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$ProjectName \
        ElastiCacheGlobalDatastoreName=$ElastiCacheGlobalDatastoreName \
        Route53HostesdZoneId=$Route53HostesdZoneId \
        Route53RecoreTtl=$Route53RecoreTtl \
        CacheHostname=$CacheHostname \
        CachePort=$CachePort \
        CacheClusterEnabled=$CacheClusterEnabled \
        CacheTlsEnabled=$CacheTlsEnabled \
        RoleName=$RoleName \
        FunctionName=$FunctionName \
        LayerVersionArn=$LayerVersionArn \
        SecurityGroupId=$SecurityGroupId \
        Subnets=$Subnets \
        EventName=$EventName \
        EventInterval=$EventInterval \
    --disable-rollback \
    --tags project=$ProjectName \
    --capabilities CAPABILITY_NAMED_IAM \
    --region $REGION
```

### Windows

``` powershell
$STACK_NAME=""
$REGION=""

$ProjectName=""                      # [REQUIRED] The name of this project.
$ElastiCacheGlobalDatastoreName=""   # [REQUIRED] The name of ElastiCache global datastore.
$Route53HostesdZoneId=""             # [REQUIRED] The id of Route53 Hosted Zone.
$Route53RecoreTtl="10"               # [optional] The ttl value of Route53 record.
$CacheHostname=""                    # [REQUIRED] The record name of Route53 Hosted Zone(ex. cache.test.lobal).
$CachePort="6379"                    # [REQUIRED] The port number to access cache clusters.
$CacheClusterEnabled="False"         # (False, True) [REQUIRED] Enable or disable Elasticache Cluster.
$CacheTlsEnabled="False"             # (False, True) [REQUIRED] Enable or disable Elasticache TLS Encryption.
$RoleName=""                         # [REQUIRED] The name of function's IAM role.
$FunctionName=""                     # [REQUIRED] The name of Lambda function.
$LayerVersionArn=""                  # [REQUIRED] The arn of Lambda layer with version.
$SecurityGroupId=""                  # [REQUIRED] The ID of security group for Lambda function.
$Subnets=""                          # [REQUIRED] The IDs of subnet for Lambda function.
$EventName=""                        # [REQUIRED] The name of EventBridge rule.
$EventInterval="5"                   # [REQUIRED] The number of interval time(minutes) to trigger EventBridge rule.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/elasticache/multi-az/failover/template.yaml

aws cloudformation deploy `
    --template-file template.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ProjectName=$ProjectName `
        ElastiCacheGlobalDatastoreName=$ElastiCacheGlobalDatastoreName `
        Route53HostesdZoneId=$Route53HostesdZoneId `
        Route53RecoreTtl=$Route53RecoreTtl `
        CacheHostname=$CacheHostname `
        CachePort=$CachePort `
        CacheClusterEnabled=$CacheClusterEnabled `
        CacheTlsEnabled=$CacheTlsEnabled `
        RoleName=$RoleName `
        FunctionName=$FunctionName `
        LayerVersionArn=$LayerVersionArn `
        SecurityGroupId=$SecurityGroupId `
        Subnets=$Subnets `
        EventName=$EventName `
        EventInterval=$EventInterval `
    --disable-rollback `
    --tags project=$ProjectName `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION
```

## Test Failover using AWS CLI

### Linux

``` bash
GLOBAL_DATASTORE_NAME=""
PRIMARY_REGION=""
PRIMARY_CLUSTER_NAME=""

aws elasticache failover-global-replication-group \
    --global-replication-group-id $GLOBAL_DATASTORE_NAME \
    --primary-region $PRIMARY_REGION \
    --primary-replication-group-id $PRIMARY_CLUSTER_NAME \
    --region $PRIMARY_REGION
```

### Windows

``` powershell
$GLOBAL_DATASTORE_NAME=""
$PRIMARY_REGION=""
$PRIMARY_CLUSTER_NAME=""

aws elasticache failover-global-replication-group `
    --global-replication-group-id $GLOBAL_DATASTORE_NAME `
    --primary-region $PRIMARY_REGION `
    --primary-replication-group-id $PRIMARY_CLUSTER_NAME `
    --region $PRIMARY_REGION
```