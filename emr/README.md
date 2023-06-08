# EMR

## EMR on EKS

### Linux

``` bash
STACK_NAME="<stack name>"
PROJECT_NAME="<project name>"
REGION="<region code>"

### EMR Configuration - General
VirtualClusterName=""   # [REQUIRED] The name of EMR virtual cluster.

### EMR Configuration - EKS
EksClusterName=""       # [REQUIRED] The name of EKS cluster.
NamespaceName=""        # [REQUIRED] The name of Kubernetes' namespace which you want to use EMR.

### EMR Configuration - Job Role
RoleName=""             # [REQUIRED] The name of job role.

aws cloudformation deploy \
    --template-file ./emr-container.yaml \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        VirtualClusterName=$VirtualClusterName \
        EksClusterName=$EksClusterName \
        NamespaceName=$NamespaceName \
        RoleName=$RoleName \
    --tags project=$PROJECT_NAME \
    --disable-rollback \
    --region $REGION
```

### Windows

``` powershell
$STACK_NAME="<stack name>"
$PROJECT_NAME="<project name>"
$REGION="<region code>"

### EMR Configuration - General
$VirtualClusterName=""   # [REQUIRED] The name of EMR virtual cluster.

### EMR Configuration - EKS
$EksClusterName=""       # [REQUIRED] The name of EKS cluster.
$NamespaceName=""        # [REQUIRED] The name of Kubernetes' namespace which you want to use EMR.

### EMR Configuration - Job Role
$RoleName=""             # [REQUIRED] The name of job role.

aws cloudformation deploy `
    --template-file ./emr-container.yaml `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        VirtualClusterName=$VirtualClusterName `
        EksClusterName=$EksClusterName `
        NamespaceName=$NamespaceName `
        RoleName=$RoleName `
    --tags project=$PROJECT_NAME `
    --disable-rollback `
    --region $REGION
```