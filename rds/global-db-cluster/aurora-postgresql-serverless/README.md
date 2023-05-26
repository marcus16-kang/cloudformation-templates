# Aurora PostgreSQL Instance

- [Aurora PostgreSQL Instance](#aurora-postgresql-instance)
  - [Note](#note)
    - [Cluster Parameter Group Family](#cluster-parameter-group-family)
    - [Engine Version](#engine-version)
  - [Primary](#primary)
    - [Linux](#linux)
    - [Windows](#windows)
  - [Replica](#replica)
    - [Linux](#linux-1)
    - [Windows](#windows-1)

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

## Primary

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

### Global Cluster Configuration
GlobalClusterIdentifier=""      # [REQUIRED] Identifier(name) used for global database cluster.

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

### Instance Configuration
InstanceClass=""                # [REQUIRED] Type of database instance type.
Instance1Identifier=""          # [REQUIRED] Identifier(name) used for database instance 1 (maybe writer)
Instance2Identifier=""          # [REQUIRED] Identifier(name) used for database instance 2 (maybe reader)
MonitoringRoleName=""           # [REQUIRED] Name of database monitoring iam role.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/global-db-cluster/aurora-postgresql-instance/aurora-primary.yaml

aws cloudformation deploy \
    --template-file ./aurora-primary.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        SubnetGroupName=$SubnetGroupName \
        Subnets=$Subnets \
        SecurityGroupIds=$SecurityGroupIds \
        ClusterParameterGroupName=$ClusterParameterGroupName \
        ParameterGroupName=$ParameterGroupName \
        ClusterParameterGroupFamily=$ClusterParameterGroupFamily \
        GlobalClusterIdentifier=$GlobalClusterIdentifier \
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
        InstanceClass=$InstanceClass \
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

### Global Cluster Configuration
$GlobalClusterIdentifier=""     # [REQUIRED] Identifier(name) used for global database cluster.

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

### Instance Configuration
$InstanceClass=""               # [REQUIRED] Type of database instance type.
$Instance1Identifier=""         # [REQUIRED] Identifier(name) used for database instance 1 (maybe writer)
$Instance2Identifier=""         # [REQUIRED] Identifier(name) used for database instance 2 (maybe reader)
$MonitoringRoleName=""          # [REQUIRED] Name of database monitoring iam role.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/global-db-cluster/aurora-postgresql-instance/aurora-primary.yaml

aws cloudformation deploy `
    --template-file ./aurora-primary.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        SubnetGroupName=$SubnetGroupName `
        Subnets=$Subnets `
        SecurityGroupIds=$SecurityGroupIds `
        ClusterParameterGroupName=$ClusterParameterGroupName `
        ParameterGroupName=$ParameterGroupName `
        ClusterParameterGroupFamily=$ClusterParameterGroupFamily `
        GlobalClusterIdentifier=$GlobalClusterIdentifier `
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
        InstanceClass=$InstanceClass `
        Instance1Identifier=$Instance1Identifier `
        Instance2Identifier=$Instance2Identifier `
        MonitoringRoleName=$MonitoringRoleName `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION_CODE
```

## Replica

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

### Global Cluster Configuration
GlobalClusterIdentifier=""      # [REQUIRED] Identifier(name) used for global database cluster.

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

### Instance Configuration
InstanceClass=""                # [REQUIRED] Type of database instance type.
Instance1Identifier=""          # [REQUIRED] Identifier(name) used for database instance 1 (maybe writer)
Instance2Identifier=""          # [REQUIRED] Identifier(name) used for database instance 2 (maybe reader)
MonitoringRoleName=""           # [REQUIRED] Name of database monitoring iam role.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/global-db-cluster/aurora-postgresql-instance/aurora-replica.yaml

aws cloudformation deploy \
    --template-file ./aurora-replica.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        SubnetGroupName=$SubnetGroupName \
        Subnets=$Subnets \
        SecurityGroupIds=$SecurityGroupIds \
        ClusterParameterGroupName=$ClusterParameterGroupName \
        ParameterGroupName=$ParameterGroupName \
        ClusterParameterGroupFamily=$ClusterParameterGroupFamily \
        GlobalClusterIdentifier=$GlobalClusterIdentifier \
        ClusterIdentifier=$ClusterIdentifier \
        EngineVersion=$EngineVersion \
        KmsKeyId=$KmsKeyId \
        DeletionProtection=$DeletionProtection \
        VpcId=$VpcId \
        Port=$Port \
        CreateSecurityGroup=$CreateSecurityGroup \
        SecurityGroupNameOrId=$SecurityGroupNameOrId \
        CreateSecurityGroup=$CreateSecurityGroup \
        InstanceClass=$InstanceClass \
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

### Global Cluster Configuration
$GlobalClusterIdentifier=""     # [REQUIRED] Identifier(name) used for global database cluster.

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

### Instance Configuration
$InstanceClass=""               # [REQUIRED] Type of database instance type.
$Instance1Identifier=""         # [REQUIRED] Identifier(name) used for database instance 1 (maybe writer)
$Instance2Identifier=""         # [REQUIRED] Identifier(name) used for database instance 2 (maybe reader)
$MonitoringRoleName=""          # [REQUIRED] Name of database monitoring iam role.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/global-db-cluster/aurora-postgresql-instance/aurora-replica.yaml

aws cloudformation deploy `
    --template-file ./aurora-replica.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        SubnetGroupName=$SubnetGroupName `
        Subnets=$Subnets `
        SecurityGroupIds=$SecurityGroupIds `
        ClusterParameterGroupName=$ClusterParameterGroupName `
        ParameterGroupName=$ParameterGroupName `
        ClusterParameterGroupFamily=$ClusterParameterGroupFamily `
        GlobalClusterIdentifier=$GlobalClusterIdentifier `
        ClusterIdentifier=$ClusterIdentifier `
        EngineVersion=$EngineVersion `
        KmsKeyId=$KmsKeyId `
        DeletionProtection=$DeletionProtection `
        VpcId=$VpcId `
        Port=$Port `
        CreateSecurityGroup=$CreateSecurityGroup `
        SecurityGroupNameOrId=$SecurityGroupNameOrId `
        CreateSecurityGroup=$CreateSecurityGroup `
        InstanceClass=$InstanceClass `
        Instance1Identifier=$Instance1Identifier `
        Instance2Identifier=$Instance2Identifier `
        MonitoringRoleName=$MonitoringRoleName `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION_CODE
```