# EKS Security Groups

> You can check rules [here](https://marcus16-kang.github.io/aws-resources-example/Containers/EKS/17-cluster-and-nodegroup-security-control/).

## Deploy

### Linux

``` bash
STACK_NAME=""
PROJECT_NAME=""
REGION=""

ClusterSecurityGroup=""             # [REQUIRED] The Id of EKS Cluster Security Group.
AdditionalClusterSecurityGroup=""   # [REQUIRED] The Id of EKS Additional Cluster Security Group.
GeneralNodegroupSecurityGroup=""    # [REQUIRED] The Id of EKS General Nodegroup Security Group.
BastionInstanceSecurityGroup=""     # [optional] The Id of Bastion Instance Security Group.
VpcEndpointSecurityGroup=""         # [optional] The Id of VPC Endpoint Security Group.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/security-group/security-group-rules.yaml

aws cloudformation deploy \
    --template-file ./security-group-rules.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ClusterSecurityGroup=$ClusterSecurityGroup \
        AdditionalClusterSecurityGroup=$AdditionalClusterSecurityGroup \
        GeneralNodegroupSecurityGroup=$GeneralNodegroupSecurityGroup \
        BastionInstanceSecurityGroup=$BastionInstanceSecurityGroup \
        VpcEndpointSecurityGroup=$VpcEndpointSecurityGroup \
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
$BastionInstanceSecurityGroup=""     # [optional] The Id of Bastion Instance Security Group.
$VpcEndpointSecurityGroup=""         # [optional] The Id of VPC Endpoint Security Group.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/security-group/security-group-rules.yaml

aws cloudformation deploy `
    --template-file ./security-group-rules.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ClusterSecurityGroup=$ClusterSecurityGroup `
        AdditionalClusterSecurityGroup=$AdditionalClusterSecurityGroup `
        GeneralNodegroupSecurityGroup=$GeneralNodegroupSecurityGroup `
        BastionInstanceSecurityGroup=$BastionInstanceSecurityGroup `
        VpcEndpointSecurityGroup=$VpcEndpointSecurityGroup `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --region $REGION
```