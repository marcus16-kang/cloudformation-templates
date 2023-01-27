# EKS

## Deploy the Kubernetes public extensions

**Linux**

``` shell
STACK_NAME=<stack name>
REGION=<region code>

wget https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/resource-provider.yaml
aws cloudformation deploy \
    --template-file ./resource-provider.yaml \
    --stack-name $STACK_NAME \
    --capabilities CAPABILITY_IAM \
    --region $REGION
```

**Windows**

``` powershell
$STACK_NAME="<stack name>"
$REGION="<region code>"

Invoke-WebRequest -OutFile resource-provider.yaml `
    https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/resource-provider.yaml
aws cloudformation deploy `
    --template-file ./resource-provider.yaml `
    --stack-name $STACK_NAME `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION
```