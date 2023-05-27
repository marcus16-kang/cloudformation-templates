# Aurora MySQL 8.0 Instance

- [Aurora MySQL 8.0 Instance](#aurora-mysql-80-instance)
  - [Note](#note)
    - [Engine Version](#engine-version)
    - [Instance Type](#instance-type)
  - [Commands](#commands)
    - [Linux](#linux)
    - [Windows](#windows)

## Note

### Engine Version

- `8.0.mysql_aurora.3.01.0`
- `8.0.mysql_aurora.3.01.1`
- `8.0.mysql_aurora.3.02.0`
- `8.0.mysql_aurora.3.02.1`
- `8.0.mysql_aurora.3.02.2`
- `8.0.mysql_aurora.3.02.3`
- `8.0.mysql_aurora.3.03.0`
- `8.0.mysql_aurora.3.03.1`

### Instance Type

<details>
<summary><code>r5</code> series</summary>

- `db.r5.large`
- `db.r5.xlarge`
- `db.r5.2xlarge`
- `db.r5.4xlarge`
- `db.r5.8xlarge`
- `db.r5.12xlarge`
- `db.r5.16xlarge`
- `db.r5.24xlarge`

</details>

<details>
<summary><code>r6g</code> series</summary>

- `db.r6g.large`
- `db.r6g.xlarge`
- `db.r6g.2xlarge`
- `db.r6g.4xlarge`
- `db.r6g.8xlarge`
- `db.r6g.12xlarge`
- `db.r6g.16xlarge`

</details>

<details>
<summary><code>r6i</code> series</summary>

- `db.r6i.large`
- `db.r6i.xlarge`
- `db.r6i.2xlarge`
- `db.r6i.4xlarge`
- `db.r6i.8xlarge`
- `db.r6i.12xlarge`
- `db.r6i.16xlarge`
- `db.r6i.24xlarge`
- `db.r6i.32xlarge`

</details>

<details>
<summary><code>t3</code> series</summary>

- `db.t3.medium`
- `db.t3.large`

</details>

<details>
<summary><code>t4g</code> series</summary>

- `db.t4g.medium`
- `db.t4g.large`

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

### Instance Configuration
InstanceClass=""                # [REQUIRED] Type of database instance type.
Instance1Identifier=""          # [REQUIRED] Identifier(name) used for database instance 1 (maybe writer)
Instance2Identifier=""          # [REQUIRED] Identifier(name) used for database instance 2 (maybe reader)
MonitoringRoleName=""           # [REQUIRED] Name of database monitoring iam role.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/multi-az-cluster/aurora-mysql-8.0-instance/rds-cluster.yaml

aws cloudformation deploy \
    --template-file ./rds-cluster.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        SubnetGroupName=$SubnetGroupName \
        Subnets=$Subnets \
        SecurityGroupIds=$SecurityGroupIds \
        ClusterParameterGroupName=$ClusterParameterGroupName \
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

### Instance Configuration
$InstanceClass=""               # [REQUIRED] Type of database instance type.
$Instance1Identifier=""         # [REQUIRED] Identifier(name) used for database instance 1 (maybe writer)
$Instance2Identifier=""         # [REQUIRED] Identifier(name) used for database instance 2 (maybe reader)
$MonitoringRoleName=""          # [REQUIRED] Name of database monitoring iam role.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/multi-az-cluster/aurora-mysql-8.0-instance/rds-cluster.yaml

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
        InstanceClass=$InstanceClass `
        Instance1Identifier=$Instance1Identifier `
        Instance2Identifier=$Instance2Identifier `
        MonitoringRoleName=$MonitoringRoleName `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION_CODE
```