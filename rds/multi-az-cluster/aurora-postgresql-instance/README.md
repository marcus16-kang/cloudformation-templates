# Aurora PostgreSQL Instance

- [Aurora PostgreSQL Instance](#aurora-postgresql-instance)
  - [Note](#note)
    - [Cluster Parameter Group Family](#cluster-parameter-group-family)
    - [Engine Version](#engine-version)
    - [Instance Type](#instance-type)
  - [Commands](#commands)
    - [Linux](#linux)
    - [Windows](#windows)

## Note

### Cluster Parameter Group Family

- `aurora-postgresql11`
- `aurora-postgresql12`
- `aurora-postgresql13`
- `aurora-postgresql14`
- `aurora-postgresql15`

### Engine Version

<details>
<summary><code>11</code> versions</summary>

- `11.9`
- `11.13`
- `11.14`
- `11.15`
- `11.16`
- `11.17`
- `11.18`
- `11.19`

</details>

<details>
<summary><code>12</code> versions</summary>

- `12.8`
- `12.9`
- `12.10`
- `12.11`
- `12.12`
- `12.13`
- `12.14`

</details>

<details>
<summary><code>13</code> versions</summary>

- `13.4`
- `13.5`
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

### Instance Type

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

### Instance Configuration
InstanceClass=""                # [REQUIRED] Type of database instance type.
Instance1Identifier=""          # [REQUIRED] Identifier(name) used for database instance 1 (maybe writer)
Instance2Identifier=""          # [REQUIRED] Identifier(name) used for database instance 2 (maybe reader)
MonitoringRoleName=""           # [REQUIRED] Name of database monitoring iam role.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/multi-az-cluster/aurora-postgresql-instance/rds-cluster.yaml

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

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/rds/multi-az-cluster/aurora-postgresql-instance/rds-cluster.yaml

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
        InstanceClass=$InstanceClass `
        Instance1Identifier=$Instance1Identifier `
        Instance2Identifier=$Instance2Identifier `
        MonitoringRoleName=$MonitoringRoleName `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION_CODE
```