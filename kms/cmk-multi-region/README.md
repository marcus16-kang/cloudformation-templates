# CMK Multi Region

### Linux

``` bash
PRIMARY_REGION="<region code>"
REPLICA_REGION="<region code>"
STACK_NAME="<cloudformation stack name>"
ALIAS="<kms alias>"

aws cloudformation deploy \
    --stack-name $STACK_NAME \
    --template-file ./primary.yaml \
    --parameter-overrides KmsKeyAliasName=$ALIAS \
    --region $PRIMARY_REGION

PRIMARY_KMS_ARN=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --region $PRIMARY_REGION --query 'Stacks[0].Outputs[0].OutputValue')

aws cloudformation deploy \
    --stack-name $STACK_NAME \
    --template-file ./replica.yaml \
    --parameter-overrides KmsKeyAliasName=$ALIAS PrimaryKeyArn=$PRIMARY_KMS_ARN \
    --region $REPLICA_REGION

REPLICA_KMS_ARN=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --region $REPLICA_REGION --query 'Stacks[0].Outputs[0].OutputValue')

echo $PRIMARY_KMS_ARN
echo $REPLICA_KMS_ARN
```

### Windows

``` powershell
$PRIMARY_REGION="<region code>"
$REPLICA_REGION="<region code>"
$STACK_NAME="<cloudformation stack name>"
$ALIAS="<kms alias>"

aws cloudformation deploy `
    --stack-name $STACK_NAME `
    --template-file .\primary.yaml `
    --parameter-overrides KmsKeyAliasName=$ALIAS `
    --region $PRIMARY_REGION

$PRIMARY_KMS_ARN=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --region $PRIMARY_REGION --query 'Stacks[0].Outputs[0].OutputValue')

aws cloudformation deploy `
    --stack-name $STACK_NAME `
    --template-file .\replica.yaml `
    --parameter-overrides KmsKeyAliasName=$ALIAS PrimaryKeyArn=$PRIMARY_KMS_ARN `
    --region $REPLICA_REGION

$REPLICA_KMS_ARN=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --region $REPLICA_REGION --query 'Stacks[0].Outputs[0].OutputValue')

echo $PRIMARY_KMS_ARN
echo $REPLICA_KMS_ARN
```