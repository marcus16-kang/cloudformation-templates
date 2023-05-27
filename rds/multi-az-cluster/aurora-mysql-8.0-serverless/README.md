# Aurora MySQL 8.0 Serverless

- [Aurora MySQL 8.0 Serverless](#aurora-mysql-80-serverless)
  - [Note](#note)
    - [Engine Version](#engine-version)
  - [Commands](#commands)
    - [Linux](#linux)
    - [Windows](#windows)

## Note

### Engine Version

- `8.0.mysql_aurora.3.02.0`
- `8.0.mysql_aurora.3.02.1`
- `8.0.mysql_aurora.3.02.2`
- `8.0.mysql_aurora.3.02.3`
- `8.0.mysql_aurora.3.03.0`
- `8.0.mysql_aurora.3.03.1`

## Commands

### Linux

``` bash
STACK_NAME=""
PROJECT_NAME=""
REGION_CODE=""

### Subnet Group Configuration
SubnetGroupName=""              # [REQUIRED] he name of this launch template.
Subnets=""                      # [REQUIRED] List of database subnet ids.

### Parameter Group Configuration
ClusterParameterGroupName=""    # [REQUIRED] Name of database cluster parameter group.
ParameterGroupName=""           # [REQUIRED] Name of database parameter group.

### Cluster Configuration - General
ClusterIdentifier=""            # [REQUIRED] Identifier(name) used for database cluster.
EngineVersion=""                # [REQUIRED] EngineVersion for database. (https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-engineversion)
KmsKeyId=""                     # [optional] Arn of kms key for database cluster. (If don't specify this property, use default key.)
DeletionProtection="true"       # `false`(default) or `true` | [optional] State for database deletion protection.

### Cluster Configuration - Network
VpcId=""                        # [REQUIRED] ID of database vpc.
Port="3306"                     # [REQUIRED] Port number for database instance.
CreateSecurityGroup="Yes"       # `Yes`(default) or `No` | [REQUIRED] Create a new security group or using existed security group.
SecurityGroupNameOrId=""        # [REQUIRED] New security group name or existed security group id.

### Cluster Configuration - Credential
Username=""                     # [REQUIRED] Username for database access.
Password=""                     # [REQUIRED] Password for database access.

### Cluster Configuration - Capacity
MinCapacity=""                  # [REQUIRED] Min capacity of serverless cluster. (0.5 ~ 128)
MaxCapacity=""                  # [REQUIRED] Max capacity of serverless cluster. (1 ~ 128)

### Instance Configuration
Instance1Identifier=""          # [REQUIRED] Identifier(name) used for database instance 1 (maybe writer)
Instance2Identifier=""          # [REQUIRED] Identifier(name) used for database instance 2 (maybe reader)
MonitoringRoleName=""           # [REQUIRED] Name of database monitoring iam role.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/multi-az-cluster/aurora-mysql-8.0-serverless/rds-cluster.yaml

aws cloudformation deploy \
    --template-file ./rds-cluster.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        SubnetGroupName=$SubnetGroupName \
        Subnets=$Subnets \
        SecurityGroupIds=$SecurityGroupIds \
        ClusterParameterGroupName=$ClusterParameterGroupName \
        ParameterGroupName=$ParameterGroupName \
        ClusterIdentifier=$ClusterIdentifier \
        EngineVersion=$EngineVersion \
        KmsKeyId=$KmsKeyId \
        DeletionProtection=$DeletionProtection \
        VpcId=$VpcId \
        Port=$Port \
        CreateSecurityGroup=$CreateSecurityGroup \
        SecurityGroupNameOrId=$SecurityGroupNameOrId \
        CreateSecurityGroup=$CreateSecurityGroup \
        Username=$Username \
        Password=$Password \
        MinCapacity=$MinCapacity \
        MaxCapacity=$MaxCapacity \
        Instance1Identifier=$Instance1Identifier \
        Instance2Identifier=$Instance2Identifier \
        MonitoringRoleName=$MonitoringRoleName \
    --disable-rollback \
    --tags project=$PROJECT_NAME \
    --capabilities CAPABILITY_NAMED_IAM \
    --region $REGION_CODE
```

### Windows

``` powershell
$STACK_NAME=""
$PROJECT_NAME=""
$REGION_CODE=""

### Subnet Group Configuration
$SubnetGroupName=""             # [REQUIRED] he name of this launch template.
$Subnets=""                     # [REQUIRED] List of database subnet ids.

### Parameter Group Configuration
$ClusterParameterGroupName=""   # [REQUIRED] Name of database cluster parameter group.
$ParameterGroupName=""          # [REQUIRED] Name of database parameter group.

### Cluster Configuration - General
$ClusterIdentifier=""           # [REQUIRED] Identifier(name) used for database cluster.
$EngineVersion=""               # [REQUIRED] EngineVersion for database. (https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-engineversion)
$KmsKeyId=""                    # [optional] Arn of kms key for database cluster. (If don't specify this property, use default key.)
$DeletionProtection="true"      # `false`(default) or `true` | [optional] State for database deletion protection.

### Cluster Configuration - Network
$VpcId=""                       # [REQUIRED] ID of database vpc.
$Port="3306"                    # [REQUIRED] Port number for database instance.
$CreateSecurityGroup="Yes"      # `Yes`(default) or `No` | [REQUIRED] Create a new security group or using existed security group.
$SecurityGroupNameOrId=""       # [REQUIRED] New security group name or existed security group id.

### Cluster Configuration - Credential
$Username=""                    # [REQUIRED] Username for database access.
$Password=""                    # [REQUIRED] Password for database access.

### Cluster Configuration - Capacity
$MinCapacity=""                 # [REQUIRED] Min capacity of serverless cluster. (0.5 ~ 128)
$MaxCapacity=""                 # [REQUIRED] Max capacity of serverless cluster. (1 ~ 128)

### Instance Configuration
$Instance1Identifier=""         # [REQUIRED] Identifier(name) used for database instance 1 (maybe writer)
$Instance2Identifier=""         # [REQUIRED] Identifier(name) used for database instance 2 (maybe reader)
$MonitoringRoleName=""          # [REQUIRED] Name of database monitoring iam role.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/multi-az-cluster/aurora-mysql-8.0-serverless/rds-cluster.yaml

aws cloudformation deploy `
    --template-file ./rds-cluster.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        SubnetGroupName=$SubnetGroupName `
        Subnets=$Subnets `
        SecurityGroupIds=$SecurityGroupIds `
        ClusterParameterGroupName=$ClusterParameterGroupName `
        ParameterGroupName=$ParameterGroupName `
        ClusterIdentifier=$ClusterIdentifier `
        EngineVersion=$EngineVersion `
        KmsKeyId=$KmsKeyId `
        DeletionProtection=$DeletionProtection `
        VpcId=$VpcId `
        Port=$Port `
        CreateSecurityGroup=$CreateSecurityGroup `
        SecurityGroupNameOrId=$SecurityGroupNameOrId `
        CreateSecurityGroup=$CreateSecurityGroup `
        Username=$Username `
        Password=$Password `
        MinCapacity=$MinCapacity `
        MaxCapacity=$MaxCapacity `
        Instance1Identifier=$Instance1Identifier `
        Instance2Identifier=$Instance2Identifier `
        MonitoringRoleName=$MonitoringRoleName `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION_CODE
```