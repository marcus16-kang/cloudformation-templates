# Aurora PostgreSQL Serverless

- [Aurora PostgreSQL Serverless](#aurora-postgresql-serverless)
  - [Note](#note)
    - [Cluster Parameter Group Family](#cluster-parameter-group-family)
    - [Engine Version](#engine-version)
  - [Commands](#commands)
    - [Linux](#linux)
    - [Windows](#windows)

## Note

### Cluster Parameter Group Family

- `aurora-postgresql13`
- `aurora-postgresql14`
- `aurora-postgresql15`

### Engine Version

<details>
<summary><code>13</code> versions</summary>

- `13.6`
- `13.7`
- `13.8`
- `13.9`
- `13.10`

</details>

<details>
<summary><code>14</code> versions</summary>

- `14.3`
- `14.4`
- `14.5`
- `14.6`
- `14.7`

</details>

<details>
<summary><code>15</code> versions</summary>

- `15.2`

</details>

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
ClusterParameterGroupFamily=""  # [REQUIRED] Name of database cluster parameter group family.

### Cluster Configuration - General
ClusterIdentifier=""            # [REQUIRED] Identifier(name) used for database cluster.
EngineVersion=""                # [REQUIRED] EngineVersion for database. (https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-engineversion)
KmsKeyId=""                     # [optional] Arn of kms key for database cluster. (If don't specify this property, use default key.)
DeletionProtection="true"       # `false`(default) or `true` | [optional] State for database deletion protection.

### Cluster Configuration - Network
VpcId=""                        # [REQUIRED] ID of database vpc.
Port="5432"                     # [REQUIRED] Port number for database instance.
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

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/multi-az-cluster/aurora-postgresql-serverless/rds-cluster.yaml

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
        ClusterParameterGroupFamily=$ClusterParameterGroupFamily \
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
$ClusterParameterGroupFamily="" # [REQUIRED] Name of database cluster parameter group family.

### Cluster Configuration - General
$ClusterIdentifier=""           # [REQUIRED] Identifier(name) used for database cluster.
$EngineVersion=""               # [REQUIRED] EngineVersion for database. (https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-engineversion)
$KmsKeyId=""                    # [optional] Arn of kms key for database cluster. (If don't specify this property, use default key.)
$DeletionProtection="true"      # `false`(default) or `true` | [optional] State for database deletion protection.

### Cluster Configuration - Network
$VpcId=""                       # [REQUIRED] ID of database vpc.
$Port="5432"                    # [REQUIRED] Port number for database instance.
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

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/multi-az-cluster/aurora-postgresql-serverless/rds-cluster.yaml

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
        ClusterParameterGroupFamily=$ClusterParameterGroupFamily `
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