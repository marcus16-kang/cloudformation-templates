# RDS Single DB Instance

## Parameters

### `Engine` and `EngineVersion`

- `mariadb`
  - `10.3.34`
  - `10.3.35`
  - `10.3.36`
  - `10.3.37`
  - `10.4.24`
  - `10.4.25`
  - `10.4.26`
  - `10.4.27`
  - `10.5.12`
  - `10.5.13`
  - `10.5.15`
  - `10.5.16`
  - `10.5.17`
  - `10.5.18`
  - `10.6.5`
  - `10.6.7`
  - `10.6.8`
  - `10.6.10` (default)
  - `10.6.11`
- `mysql`
  - `5.7.33`
  - `5.7.34`
  - `5.7.37`
  - `5.7.38`
  - `5.7.39`
  - `5.7.40`
  - `8.0.23`
  - `8.0.25`
  - `8.0.26`
  - `8.0.27`
  - `8.0.28`
  - `8.0.30`
  - `8.0.31`
- `oracle-ee`, `oracle-ee-cdb`, `oracle-se2`, `oracle-se2-cdb`
  - `21.0.0.0.ru-2022-10.rur-2022-10.r1`
  - `21.0.0.0.ru-2022-07.rur-2022-07.r1`
  - `21.0.0.0.ru-2022-04.rur-2022-04.r1`
  - `21.0.0.0.ru-2022-01.rur-2022-01.r1`
  - `19.0.0.0.ru-2022-10.rur-2022-10.r1` (default)
  - `19.0.0.0.ru-2022-07.rur-2022-07.r1`
  - `19.0.0.0.ru-2022-04.rur-2022-04.r1`
  - `19.0.0.0.ru-2022-01.rur-2022-01.r1`
  - `19.0.0.0.ru-2021-10.rur-2021-10.r1`
  - `19.0.0.0.ru-2021-07.rur-2021-07.r1`
  - `19.0.0.0.ru-2021-04.rur-2021-04.r1`
  - `19.0.0.0.ru-2021-01.rur-2021-01.r2`
  - `19.0.0.0.ru-2021-01.rur-2021-01.r1`
  - `19.0.0.0.ru-2020-10.rur-2020-10.r1`
  - `19.0.0.0.ru-2020-07.rur-2020-07.r1`
  - `19.0.0.0.ru-2020-04.rur-2020-04.r1`
  - `19.0.0.0.ru-2020-01.rur-2020-01.r1`
  - `19.0.0.0.ru-2019-10.rur-2019-10.r1`
  - `19.0.0.0.ru-2019-07.rur-2019-07.r1`
- `postgres`
  - `10.17`
  - `10.18`
  - `10.19`
  - `10.20`
  - `10.21`
  - `10.22`
  - `11.12`
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
  - `14.1`
  - `14.2`
  - `14.3`
  - `14.4`
  - `14.5`
- `sqlserver-ee`, `sqlserver-se`, `sqlserver-ex`, `sqlserver-web`
  - `15.00.4236.7.v1`
  - `15.00.4198.2.v1`
  - `15.00.4153.1.v1`
  - `15.00.4073.23.v1`
  - `15.00.4043.16.v1`
  - `14.00.3451.2.v1`
  - `14.00.3421.10.v1`
  - `14.00.3401.7.v1`
  - `14.00.3381.3.v1`
  - `14.00.3356.20.v1`
  - `14.00.3294.2.v1`
  - `14.00.3281.6.v1`
  - `13.00.6419.1.v1`
  - `13.00.6300.2.v1`
  - `12.00.6439.10.v1`
  - `12.00.6433.1.v1`
  - `12.00.6329.1.v1`
  - `12.00.6293.0.v1`

### `ParameterGroupFamily`

- `mariadb`
  - `mariadb10.3`
  - `mariadb10.4`
  - `mariadb10.5`
  - `mariadb10.6`
- `mysql`
  - `mysql5.7`
  - `mysql8.0`
- `oracle`
  - `oracle-ee-19`
  - `oracle-ee-cdb-19`
  - `oracle-ee-cdb-21`
  - `oracle-se2-19`
  - `oracle-se2-cdb-19`
  - `oracle-se2-cdb-21`
- `postgres`
  - `postgres10`
  - `postgres11`
  - `postgres12`
  - `postgres13`
  - `postgres14`
- `sqlserver`
  - `sqlserver-ee-12.0`
  - `sqlserver-ee-13.0`
  - `sqlserver-ee-14.0`
  - `sqlserver-ee-15.0`
  - `sqlserver-ex-12.0`
  - `sqlserver-ex-13.0`
  - `sqlserver-ex-14.0`
  - `sqlserver-ex-15.0`
  - `sqlserver-se-12.0`
  - `sqlserver-se-13.0`
  - `sqlserver-se-14.0`
  - `sqlserver-se-15.0`
  - `sqlserver-web-12.0`
  - `sqlserver-web-13.0`
  - `sqlserver-web-14.0`
  - `sqlserver-web-15.0`
  - `custom-sqlserver-ee-15.0`
  - `custom-sqlserver-se-15.0`
  - `custom-sqlserver-web-15.0`

### `OptionGroupMajorVersion`

- `mariadb`
  - `10.0`
  - `10.1`
  - `10.2`
  - `10.3`
  - `10.4`
  - `10.5`
  - `10.6`
- `mysql`
  - `5.6`
  - `5.7`
  - `8.0`
- `oracle-ee`
  - `19`
- `oracle-ee-cdb`
  - `19`
  - `21`
- `oracle-se2`
  - `19`
- `oracle-se2-cdb`
  - `19`
  - `21`
- `sqlserver`
  - `11.00`
  - `12.00`
  - `13.00`
  - `14.00`
  - `15.00`


### `DBInstanceClass`

[Amazon RDS Instance Types](https://aws.amazon.com/ko/rds/instance-types/)


## Scripts

### Linux

``` bash
### Common Parameters - RDS Informations
# ALLOCATED_STORAGE="<database allocated storage amount>"
# IOPS="<database storage iops>"
# MAX_ALLOCATED_STORAGE="<database max allocated storage amount>"
PARAMETER_GROUP_FAMILY="<database parameter group family>"
PARAMETER_GROUP_NAME="<database parameter group name>"
# OPTION_GROUP_NAME="<database option group name>"                     # PostgreSQL doesn't need option group
# OPTION_GROUP_MAJOR_VERSION="<database option group major version>"  # PostgreSQL doesn't need option group
SUBNET_GROUP_NAME="<database subnet group name>"
INSTANCE_CLASS="<database instance class>"
INSTANCE_IDENTIFIER="<database instance name>"
MONITORING_ROLE="<database monitoring iam role name>"
# KMS_KEY_ID="<database encryption kms cmk id>"
# DELETION_PROTECTION="<database deletion protection (true or false)>"


### Common Parameters - Network Informations
SUBNETS="<subnet ids with comma>"
SECURITY_GROUP_NAME="<database security group name>"
VPC_ID="<vpc id>"

### Common Parameters - Database Informations
DB_NAME="<database name>"
ENGINE="<database engine>"
ENGINE_VERSION="<database engine version>"
USERNAME="<database root user name>"
PASSWORD="<database root user password>"
PORT="<database port>"  # MySQL: 3306, PostgreSQL: 5432, Oracle: 1521, SQLServer: 1433

### CloudFormation Parameters
STACK_NAME="<cloudformation stack name>"
REGION="<cloudformation region code>"


aws cloudformation deploy \
    --stack-name $STACK_NAME \
    --template-file ./instance.yaml \
    --parameter-overrides \
        # AllocatedStorage=$ALLOCATED_STORAGE \
        DBName=$DB_NAME \
        Engine=$ENGINE \
        EngineVersion=$ENGINE_VERSION \
        # Iops=$IOPS \
        # MaxAllocatedStorage=$MAX_ALLOCATED_STORAGE \
        ParameterGroupFamily=$PARAMETER_GROUP_FAMILY \
        ParameterGroupName=$PARAMETER_GROUP_NAME \
        # OptionGroupName=$OPTION_GROUP_NAME \
        # OptionGroupMajorVersion=$OPTION_GROUP_MAJOR_VERSION \
        SubnetGroupName=$SUBNET_GROUP_NAME \
        Subnets=$SUBNETS \
        SecurityGroupName=$SECURITY_GROUP_NAME \
        VpcId=$VPC_ID \
        InstanceClass=$INSTANCE_CLASS \
        InstanceIdentifier=$INSTANCE_IDENTIFIER \
        Port=$PORT \
        MonitoringRole=$MONITORING_ROLE \
        # KmsKeyId=$KMS_KEY_ID \
        username=$USERNAME \
        password=$PASSWORD \
        # DeletionProtection=$DELETION_PROTECTION \
    --capabilities CAPABILITY_NAMED_IAM \
    --region $REGION
```

### Windows

``` powershell
### Common Parameters - RDS Informations
# $ALLOCATED_STORAGE="<database allocated storage amount>"
# $IOPS="<database storage iops>"
# $MAX_ALLOCATED_STORAGE="<database max allocated storage amount>"
$PARAMETER_GROUP_FAMILY="<database parameter group family>"
$PARAMETER_GROUP_NAME="<database parameter group name>"
# $OPTION_GROUP_NAME="<database option group name>"                     # PostgreSQL doesn't need option group
# $OPTION_GROUP_MAJOR_VERSION="<database option group major version>"  # PostgreSQL doesn't need option group
$SUBNET_GROUP_NAME="<database subnet group name>"
$INSTANCE_CLASS="<database instance class>"
$INSTANCE_IDENTIFIER="<database instance name>"
$MONITORING_ROLE="<database monitoring iam role name>"
# $KMS_KEY_ID="<database encryption kms cmk id>"
# $DELETION_PROTECTION="<database deletion protection (true or false)>"


### Common Parameters - Network Informations
$SUBNETS="<subnet ids with comma>"
$SECURITY_GROUP_NAME="<database security group name>"
$VPC_ID="<vpc id>"

### Common Parameters - Database Informations
$DB_NAME="<database name>"
$ENGINE="<database engine>"
$ENGINE_VERSION="<database engine version>"
$USERNAME="<database root user name>"
$PASSWORD="<database root user password>"
$PORT="<database port>"  # MySQL: 3306, PostgreSQL: 5432, Oracle: 1521, SQLServer: 1433

### CloudFormation Parameters
$STACK_NAME="<cloudformation stack name>"
$REGION="<cloudformation region code>"


aws cloudformation deploy `
    --stack-name $STACK_NAME `
    --template-file ./instance.yaml `
    --parameter-overrides `
        # AllocatedStorage=$ALLOCATED_STORAGE `
        DBName=$DB_NAME `
        Engine=$ENGINE `
        EngineVersion=$ENGINE_VERSION `
        # Iops=$IOPS `
        # MaxAllocatedStorage=$MAX_ALLOCATED_STORAGE `
        ParameterGroupFamily=$PARAMETER_GROUP_FAMILY `
        ParameterGroupName=$PARAMETER_GROUP_NAME `
        # OptionGroupName=$OPTION_GROUP_NAME `
        # OptionGroupMajorVersion=$OPTION_GROUP_MAJOR_VERSION `
        SubnetGroupName=$SUBNET_GROUP_NAME `
        Subnets=$SUBNETS `
        SecurityGroupName=$SECURITY_GROUP_NAME `
        VpcId=$VPC_ID `
        InstanceClass=$INSTANCE_CLASS `
        InstanceIdentifier=$INSTANCE_IDENTIFIER `
        Port=$PORT `
        MonitoringRole=$MONITORING_ROLE `
        # KmsKeyId=$KMS_KEY_ID `
        username=$USERNAME `
        password=$PASSWORD `
        # DeletionProtection=$DELETION_PROTECTION `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION
```