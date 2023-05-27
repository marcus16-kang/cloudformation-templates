# Aurora MySQL 5.7

- [Aurora MySQL 5.7](#aurora-mysql-57)
  - [Note](#note)
    - [Engine Version](#engine-version)
    - [Instance Type](#instance-type)
  - [Commands](#commands)
    - [Linux](#linux)
    - [Windows](#windows)

## Note

### Engine Version

- `5.7.mysql_aurora.2.07.0`
- `5.7.mysql_aurora.2.07.1`
- `5.7.mysql_aurora.2.07.2`
- `5.7.mysql_aurora.2.07.3`
- `5.7.mysql_aurora.2.07.4`
- `5.7.mysql_aurora.2.07.5`
- `5.7.mysql_aurora.2.07.6`
- `5.7.mysql_aurora.2.07.7`
- `5.7.mysql_aurora.2.07.8`
- `5.7.mysql_aurora.2.07.9`
- `5.7.mysql_aurora.2.11.1`
- `5.7.mysql_aurora.2.11.2`

### Instance Type

<details>
<summary><code>r3</code> series</summary>

- `db.r3.large`
- `db.r3.xlarge`
- `db.r3.2xlarge`
- `db.r3.4xlarge`
- `db.r3.8xlarge`

</details>

<details>
<summary><code>r4</code> series</summary>

- `db.r4.large`
- `db.r4.xlarge`
- `db.r4.2xlarge`
- `db.r4.4xlarge`
- `db.r4.8xlarge`
- `db.r4.16xlarge`

</details>

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
<summary><code>t2</code> series</summary>

- `db.t2.small`
- `db.t2.medium`
- `db.t2.large`

</details>

<details>
<summary><code>t3</code> series</summary>

- `db.t3.small`
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

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/multi-az-cluster/aurora-mysql-5.7/rds-cluster.yaml

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

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/multi-az-cluster/aurora-mysql-5.7/rds-cluster.yaml

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