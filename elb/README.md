# ELB Templates

- [ELB Templates](#elb-templates)
  - [Application Load Balancer](#application-load-balancer)
    - [Linux](#linux)
    - [Windows](#windows)
  - [Access Log Bucket](#access-log-bucket)
    - [Linux](#linux-1)
    - [Windows](#windows-1)

## Application Load Balancer

### Linux

``` bash
STACK_NAME="<stack name>"
PROJECT_NAME="<project name>"
REGION="<region code>"

### ALB Configuration - General
LoadBalancerName=""         # [REQUIRED] The name of alb.
VpcId=""                    # [REQUIRED] The id of alb security group's vpc.
Subnets=""                  # [REQUIRED] The id list of alb's subnets.
Scheme="internet-facing"    # `internet-facing`(default) or `internal` | [REQUIRED] The type of alb.
IpAddressType="ipv4"        # `ipv4`(default) or `dualstack` | [optional] The IP address type of alb.
SecurityGroupId=""          # [REQUIRED] The id of alb security group.
ListenerPathPattern=""      # [REQUIRED] The path pattern list of listener. Type with comma(,).  For example, `/v1/test1,/v1/admin*,/v2/test1`.

### ALB Configuration - Target Group
TargetGroupName=""          # [REQUIRED] The name of target group.
TargetType=""               # `instance`, `ip`, `lambda` or `alb` | [REQUIRED] the type of target group.
TargetSecurityGroupId=""    # [optional] The id of alb target group's security group.
TargetPort="80"             # [REQUIRED] The port number of target group.
HealthCheckPath="/"         # [REQUIRED] The health check path of target group. It should end with `/`.

### ALB Configuration - Access Log
CreateAccessLogBucket=""    # `Yes`(default) or `No` | [REQUIRED] Create a new S3 bucket or using existed S3 bucket.
AccessLogBucketName=""      # [REQUIRED] The name of alb access log bucket.
AccessLogPrefix=""          # [optional] The prefix of alb access log. It cannot start or end with `/`.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/elb/application-load-balancer.yaml

# Using `deploy`
aws cloudformation deploy \
    --template-file ./application-load-balancer.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        LoadBalancerName=$LoadBalancerName \
        VpcId=$VpcId \
        Subnets=$Subnets \
        Scheme=$Scheme \
        IpAddressType=$IpAddressType \
        SecurityGroupId=$SecurityGroupId \
        ListenerPathPattern=$ListenerPathPattern \
        TargetGroupName=$TargetGroupName \
        TargetType=$TargetType \
        TargetSecurityGroupId=$TargetSecurityGroupId \
        TargetPort=$TargetPort \
        HealthCheckPath=$HealthCheckPath \
        CreateAccessLogBucket=$CreateAccessLogBucket \
        AccessLogBucketName=$AccessLogBucketName \
        AccessLogPrefix=$AccessLogPrefix \
    --disable-rollback \
    --tags project=$PROJECT_NAME \
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack \
    --template-body file://application-load-balancer.yaml \
    --stack-name $STACK_NAME \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME \
        ParameterKey=LoadBalancerName,ParameterValue=$LoadBalancerName \
        ParameterKey=VpcId,ParameterValue=$VpcId \
        ParameterKey=Subnets,ParameterValue=$Subnets \
        ParameterKey=Scheme,ParameterValue=$Scheme \
        ParameterKey=IpAddressType,ParameterValue=$IpAddressType \
        ParameterKey=SecurityGroupId,ParameterValue=$SecurityGroupId \
        ParameterKey=ListenerPathPattern,ParameterValue=$ListenerPathPattern \
        ParameterKey=TargetGroupName,ParameterValue=$TargetGroupName \
        ParameterKey=TargetType,ParameterValue=$TargetType \
        ParameterKey=TargetSecurityGroupId,ParameterValue=$TargetSecurityGroupId \
        ParameterKey=TargetPort,ParameterValue=$TargetPort \
        ParameterKey=HealthCheckPath,ParameterValue=$HealthCheckPath \
        ParameterKey=CreateAccessLogBucket,ParameterValue=$CreateAccessLogBucket \
        ParameterKey=AccessLogBucketName,ParameterValue=$AccessLogBucketName \
        ParameterKey=AccessLogPrefix,ParameterValue=$AccessLogPrefix \
    --disable-rollback \
    --tags Key=project,Value=$PROJECT_NAME \
    --region $REGION
```

### Windows

``` powershell
$STACK_NAME="<stack name>"
$PROJECT_NAME="<project name>"
$REGION="<region code>"

### ALB Configuration - General
$LoadBalancerName=""        # [REQUIRED] The name of alb.
$VpcId=""                   # [REQUIRED] The id of alb security group's vpc.
$Subnets=""                 # [REQUIRED] The id list of alb's subnets.
$Scheme="internet-facing"   # `internet-facing`(default) or `internal` | [REQUIRED] The type of alb.
$IpAddressType="ipv4"       # `ipv4`(default) or `dualstack` | [optional] The IP address type of alb.
$SecurityGroupId=""         # [REQUIRED] The id of alb security group.
$ListenerPathPattern=""     # [REQUIRED] The path pattern list of listener. Type with comma(,).  For example, `/v1/test1,/v1/admin*,/v2/test1`.

### ALB Configuration - Target Group
$TargetGroupName=""         # [REQUIRED] The name of target group.
$TargetType=""              # `instance`, `ip`, `lambda` or `alb` | [REQUIRED] the type of target group.
$TargetSecurityGroupId=""   # [optional] The id of alb target group's security group.
$TargetPort="80"            # [REQUIRED] The port number of target group.
$HealthCheckPath="/"        # [REQUIRED] The health check path of target group. It should end with `/`.

### ALB Configuration - Access Log
$CreateAccessLogBucket=""   # `Yes`(default) or `No` | [REQUIRED] Create a new S3 bucket or using existed S3 bucket.
$AccessLogBucketName=""     # [REQUIRED] The name of alb access log bucket.
$AccessLogPrefix=""         # [optional] The prefix of alb access log. It cannot start or end with `/`.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/elb/application-load-balancer.yaml

# Using `deploy`
aws cloudformation deploy `
    --template-file ./application-load-balancer.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        LoadBalancerName=$LoadBalancerName `
        VpcId=$VpcId `
        Subnets=$Subnets `
        Scheme=$Scheme `
        IpAddressType=$IpAddressType `
        SecurityGroupId=$SecurityGroupId `
        ListenerPathPattern=$ListenerPathPattern `
        TargetGroupName=$TargetGroupName `
        TargetType=$TargetType `
        TargetSecurityGroupId=$TargetSecurityGroupId `
        TargetPort=$TargetPort `
        HealthCheckPath=$HealthCheckPath `
        CreateAccessLogBucket=$CreateAccessLogBucket `
        AccessLogBucketName=$AccessLogBucketName `
        AccessLogPrefix=$AccessLogPrefix `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack `
    --template-body file://application-load-balancer.yaml `
    --stack-name $STACK_NAME `
    --parameters `
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME `
        ParameterKey=LoadBalancerName,ParameterValue=$LoadBalancerName `
        ParameterKey=VpcId,ParameterValue=$VpcId `
        ParameterKey=Subnets,ParameterValue=$Subnets `
        ParameterKey=Scheme,ParameterValue=$Scheme `
        ParameterKey=IpAddressType,ParameterValue=$IpAddressType `
        ParameterKey=SecurityGroupId,ParameterValue=$SecurityGroupId `
        ParameterKey=ListenerPathPattern,ParameterValue=$ListenerPathPattern `
        ParameterKey=TargetGroupName,ParameterValue=$TargetGroupName `
        ParameterKey=TargetType,ParameterValue=$TargetType `
        ParameterKey=TargetSecurityGroupId,ParameterValue=$TargetSecurityGroupId `
        ParameterKey=TargetPort,ParameterValue=$TargetPort `
        ParameterKey=HealthCheckPath,ParameterValue=$HealthCheckPath `
        ParameterKey=CreateAccessLogBucket,ParameterValue=$CreateAccessLogBucket `
        ParameterKey=AccessLogBucketName,ParameterValue=$AccessLogBucketName `
        ParameterKey=AccessLogPrefix,ParameterValue=$AccessLogPrefix `
    --disable-rollback `
    --tags Key=project,Value=$PROJECT_NAME `
    --region $REGION
```

## Access Log Bucket

### Linux

``` bash
STACK_NAME="<stack name>"
PROJECT_NAME="<project name>"
REGION="<region code>"

### Bucket Configuration
AccessLogBucketName=""  # [REQUIRED] The name of alb access log bucket.
AccessLogPrefix=""      # [optional] The prefix of alb access log. It cannot start or end with `/`.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/elb/access-log-bucket.yaml

# Using `deploy`
aws cloudformation deploy \
    --template-file ./access-log-bucket.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        AccessLogBucketName=$AccessLogBucketName \
        AccessLogPrefix=$AccessLogPrefix \
    --disable-rollback \
    --tags project=$PROJECT_NAME \
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack \
    --template-body file://access-log-bucket.yaml \
    --stack-name $STACK_NAME \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME \
        ParameterKey=AccessLogBucketName,ParameterValue=$AccessLogBucketName \
        ParameterKey=AccessLogPrefix,ParameterValue=$AccessLogPrefix \
    --disable-rollback \
    --tags Key=project,Value=$PROJECT_NAME \
    --region $REGION
```

### Windows

``` powershell
$STACK_NAME="<stack name>"
$PROJECT_NAME="<project name>"
$REGION="<region code>"

### Bucket Configuration
$AccessLogBucketName="" # [REQUIRED] The name of alb access log bucket.
$AccessLogPrefix=""     # [optional] The prefix of alb access log. It cannot start or end with `/`.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/elb/access-log-bucket.yaml

# Using `deploy`
aws cloudformation deploy `
    --template-file ./access-log-bucket.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        AccessLogBucketName=$AccessLogBucketName `
        AccessLogPrefix=$AccessLogPrefix `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack `
    --template-body file://access-log-bucket.yaml `
    --stack-name $STACK_NAME `
    --parameters `
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME `
        ParameterKey=AccessLogBucketName,ParameterValue=$AccessLogBucketName `
        ParameterKey=AccessLogPrefix,ParameterValue=$AccessLogPrefix `
    --disable-rollback `
    --tags Key=project,Value=$PROJECT_NAME `
    --region $REGION
```