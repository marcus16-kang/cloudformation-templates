# Amazon Managed Service for Prometheus Workspace

## Linux

``` bash
STACK_NAME="<stack name>"
PROJECT_NAME="<project name>"
REGION="<region code>"

WORKSPACE_NAME=""                             # [REQUIRED] The name of this APS workspace.
LOG_GROUP_NAME="/aws/vendedlogs/prometheus"   # [REQUIRED] The name of this APS workspace's log group.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/aps/workspace.yaml

aws cloudformation deploy \
    --stack-name $STACK_NAME \
    --template-file ./workspace.yaml \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        WorkspaceName=$WORKSPACE_NAME \
        LogGroupName=$LOG_GROUP_NAME \
    --tags project=$PROJECT_NAME \
    --region $REGION \
    --disable-rollback
```

## Windows

``` powershell
$STACK_NAME="<stack name>"
$PROJECT_NAME="<project name>"
$REGION="<region code>"

$WORKSPACE_NAME=""                            # [REQUIRED] The name of this APS workspace.
$LOG_GROUP_NAME="/aws/vendedlogs/prometheus"  # [REQUIRED] The name of this APS workspace's log group.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/aps/workspace.yaml

aws cloudformation deploy `
    --stack-name $STACK_NAME `
    --template-file ./workspace.yaml `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        WorkspaceName=$WORKSPACE_NAME `
        LogGroupName=$LOG_GROUP_NAME `
    --tags project=$PROJECT_NAME `
    --region $REGION `
    --disable-rollback
```