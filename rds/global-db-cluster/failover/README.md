# Aurora Failover

## Linux

``` bash
STACK_NAME=""
PROJECT_NAME=""
REGION_CODE=""

### Failover Configuration
RdsGlobalClusterName=""     # [REQUIRED] The name of RDS global cluster.
Route53HostesdZoneId=""     # [REQUIRED] The id of Route53 Hosted Zone.
Route53RecordName=""        # [REQUIRED] The record name of Route53 Hosted Zone(ex. db.test.lobal).

### Function Configuration
RoleName=""                 # [REQUIRED] The name of function's IAM role.
FunctionName=""             # [REQUIRED] The name of Lambda function.
EventName=""                # [REQUIRED] The name of EventBridge rule.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/global-db-cluster/failover/aurora-failover.yaml

aws cloudformation deploy \
    --template-file ./aurora-primary.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        SubnetGroupName=$SubnetGroupName \
        RdsGlobalClusterName=$RdsGlobalClusterName \
        Route53HostesdZoneId=$Route53HostesdZoneId \
        Route53RecordName=$Route53RecordName \
        RoleName=$RoleName \
        FunctionName=$FunctionName \
        EventName=$EventName \
    --disable-rollback \
    --tags project=$PROJECT_NAME \
    --capabilities CAPABILITY_NAMED_IAM \
    --region $REGION_CODE
```

## Windows

``` powershell
$STACK_NAME=""
$PROJECT_NAME=""
$REGION_CODE=""

### Failover Configuration
$RdsGlobalClusterName=""    # [REQUIRED] The name of RDS global cluster.
$Route53HostesdZoneId=""    # [REQUIRED] The id of Route53 Hosted Zone.
$Route53RecordName=""       # [REQUIRED] The record name of Route53 Hosted Zone(ex. db.test.lobal).

### Function Configuration
$RoleName=""                # [REQUIRED] The name of function's IAM role.
$FunctionName=""            # [REQUIRED] The name of Lambda function.
$EventName=""               # [REQUIRED] The name of EventBridge rule.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/global-db-cluster/failover/aurora-failover.yaml

aws cloudformation deploy `
    --template-file ./aurora-primary.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        SubnetGroupName=$SubnetGroupName `
        RdsGlobalClusterName=$RdsGlobalClusterName `
        Route53HostesdZoneId=$Route53HostesdZoneId `
        Route53RecordName=$Route53RecordName `
        RoleName=$RoleName `
        FunctionName=$FunctionName `
        EventName=$EventName `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION_CODE
```