# EKS Security Groups

## Deploy

### Linux

``` bash
STACK_NAME=""
PROJECT_NAME=""
REGION=""

ClusterSecurityGroup=""             # [REQUIRED] The Id of EKS Cluster Security Group.
AdditionalClusterSecurityGroup=""   # [REQUIRED] The Id of EKS Additional Cluster Security Group.
GeneralNodegroupSecurityGroup=""    # [REQUIRED] The Id of EKS General Nodegroup Security Group.

curl -O https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/security-group/security-group-rules.yaml

aws cloudformation deploy \
    --template-file ./security-group-rules.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ClusterSecurityGroup=$ClusterSecurityGroup \
        AdditionalClusterSecurityGroup=$AdditionalClusterSecurityGroup \
        GeneralNodegroupSecurityGroup=$GeneralNodegroupSecurityGroup \
    --disable-rollback \
    --tags project=$PROJECT_NAME \
    --region $REGION
```

### Windows

``` powershell
$STACK_NAME=""
$PROJECT_NAME=""
$REGION=""

$ClusterSecurityGroup=""             # [REQUIRED] The Id of EKS Cluster Security Group.
$AdditionalClusterSecurityGroup=""   # [REQUIRED] The Id of EKS Additional Cluster Security Group.
$GeneralNodegroupSecurityGroup=""    # [REQUIRED] The Id of EKS General Nodegroup Security Group.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/security-group/security-group-rules.yaml

aws cloudformation deploy `
    --template-file ./security-group-rules.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ClusterSecurityGroup=$ClusterSecurityGroup `
        AdditionalClusterSecurityGroup=$AdditionalClusterSecurityGroup `
        GeneralNodegroupSecurityGroup=$GeneralNodegroupSecurityGroup `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --region $REGION
```