# RDS(Aurora) Global Database

## Parameters

### `Engine` and `EngineVersion`

- `aurora`
  - `5.6.mysql_aurora.1.23.1`
  - `5.6.mysql_aurora.1.23.2`
  - `5.6.mysql_aurora.1.23.3`
  - `5.6.mysql_aurora.1.23.4`
- `aurora-mysql`
  - `5.7.mysql_aurora.2.09.1`
  - `5.7.mysql_aurora.2.09.2`
  - `5.7.mysql_aurora.2.09.3`
  - `5.7.mysql_aurora.2.10.0`
  - `5.7.mysql_aurora.2.10.1`
  - `5.7.mysql_aurora.2.10.2`
  - `5.7.mysql_aurora.2.10.3`
  - `5.7.mysql_aurora.2.11.0`
  - `8.0.mysql_aurora.3.01.0`
  - `8.0.mysql_aurora.3.01.1`
  - `8.0.mysql_aurora.3.02.0`
  - `8.0.mysql_aurora.3.02.1`
  - `8.0.mysql_aurora.3.02.2`
- `aurora-postgresql`
  - `10.17`
  - `10.18`
  - `10.18`
  - `10.19`
  - `10.20`
  - `10.21`
  - `11.9`
  - `11.12`
  - `11.13`
  - `11.13`
  - `11.14`
  - `11.15`
  - `11.16`
  - `11.17`
  - `12.7`
  - `12.8`
  - `12.9`
  - `12.10`
  - `12.11`
  - `12.12`
  - `13.3`
  - `13.4`
  - `13.5`
  - `13.6`
  - `13.7`
  - `13.8`
  - `14.3`
  - `14.4`
  - `14.5`

### `ParameterGroupFamily`

- `aurora5.6`
- `aurora-mysql5.7`
- `aurora-mysql8.0`
- `aurora-postgresql10`
- `aurora-postgresql11`
- `aurora-postgresql12`
- `aurora-postgresql13`
- `aurora-postgresql14`

### `DBInstanceClass`

- `db.r5.large`
- `db.r5.xlarge`
- `db.r5.2xlarge`
- `db.r5.4xlarge`
- `db.r5.8xlarge`
- `db.r5.12xlarge`
- `db.r5.16xlarge`
- `db.r5.24xlarge`
- `db.r6g.large`
- `db.r6g.xlarge`
- `db.r6g.2xlarge`
- `db.r6g.4xlarge`
- `db.r6g.8xlarge`
- `db.r6g.12xlarge`
- `db.r6g.16xlarge`
- `db.x2g.large`
- `db.x2g.xlarge`
- `db.x2g.2xlarge`
- `db.x2g.4xlarge`
- `db.x2g.8xlarge`
- `db.x2g.12xlarge`
- `db.x2g.16xlarge`

## Scripts

### Linux

``` bash
# Common Parameters
GLOBAL_CLUSTER_IDENTIFIER="<global cluster name>"
ENGINE="<database engine>"
ENGINE_VERSION="<database engine version>"
PARAMETER_GROUP_FAMILY="<parameter group family>"
CLUSTER_PARAMETER_GROUP_NAME="<database cluster parameter group name>"
PARAMEGER_GROUP_NAME="<database instance parameter group name>"
SUBNET_GROUP_NAME="<database subnet group name>"
SECURITY_GROUP_NAME="<database security group name>"
INSTANCE_CLASS="<database instance class type>"
PORT="<database port>"
MONITORING_ROLE_NAME="<database monitoring iam role name>"

# Common Parameters - Database User
USERNAME="<database root user name>"
PASSWORD="<database root user password>"

# Primary Region Parameters
PRIMARY_REGION="<region code>"
PRIMARY_VPC_ID="<vpc id>"
PRIMARY_SUBNET_IDS="<subnet ids with comma>"
PRIMARY_CLUSTER_IDENTIFIER="<database primary cluster name>"
PRIMARY_INSTANCE_1_IDENTIFIER="<database primary instance 1 name>"
PRIMARY_INSTANCE_2_IDENTIFIER="<database primary instance 2 name>"
PRIMARY_KMS_KEY_ID="<database encryption primary kms key arn>"

# Replica Region Parameters
REPLICA_REGION="<region code>"
REPLICA_VPC_ID="<vpc id>"
REPLICA_SUBNET_IDS="<subnet ids with comma>"
REPLICA_CLUSTER_IDENTIFIER="<database replica cluster name>"
REPLICA_INSTANCE_1_IDENTIFIER="<database replica instance 1 name>"
REPLICA_INSTANCE_2_IDENTIFIER="<database replica instance 2 name>"
REPLICA_KMS_KEY_ID="<database encryption replica kms key arn>"

# CloudFormation Parameters
STACK_NAME="<cloudformation stack name>"


aws cloudformation deploy \
    --stack-name $STACK_NAME \
    --template-file ./primary.yaml \
    --parameter-overrides \
        GlobalClusterIdentifier=$GLOBAL_CLUSTER_IDENTIFIER \
        Engine=$ENGINE \
        EngineVersion=$ENGINE_VERSION \
        ParameterGroupFamily=$PARAMETER_GROUP_FAMILY \
        ClusterParameterGroupName=$CLUSTER_PARAMETER_GROUP_NAME \
        ParameterGroupName=$PARAMEGER_GROUP_NAME \
        DBSubnetGroupName=$SUBNET_GROUP_NAME \
        DBSubnets=$PRIMARY_SUBNET_IDS \
        DBSecurityGroupName=$SECURITY_GROUP_NAME \
        DBVpcId=$PRIMARY_VPC_ID \
        DBInstanceClass=$INSTANCE_CLASS \
        DBClusterIdentifier=$PRIMARY_CLUSTER_IDENTIFIER \
        DBInstance1Identifier=$PRIMARY_INSTANCE_1_IDENTIFIER \
        DBInstance2Identifier=$PRIMARY_INSTANCE_2_IDENTIFIER \
        DBPort=$PORT \
        DBMonitoringRole=$MONITORING_ROLE_NAME \
        KmsKeyId=$PRIMARY_KMS_KEY_ID \
        username=$USERNAME \
        password=$PASSWORD \
    --capabilities CAPABILITY_NAMED_IAM \
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
    --parameter-overrides KmsKeyAliasName=ALIAS `
    --region $PRIMARY_REGION

$PRIMARY_KMS_ARN=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --region $PRIMARY_REGION --query 'Stacks[0].Outputs[0].OutputValue')

aws cloudformation deploy `
    --stack-name $STACK_NAME `
    --template-file .\replica.yaml `
    --parameter-overrides KmsKeyAliasName=ALIAS PrimaryKeyArn=$PRIMARY_KMS_ARN `
    --region $REPLICA_REGION

$REPLICA_KMS_ARN=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --region $REPLICA_REGION --query 'Stacks[0].Outputs[0].OutputValue')

echo $PRIMARY_KMS_ARN
echo $REPLICA_KMS_ARN
```