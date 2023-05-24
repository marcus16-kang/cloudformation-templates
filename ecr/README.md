# Elastic Container Registry (ECR)

- [Elastic Container Registry (ECR)](#elastic-container-registry-ecr)
  - [Repository](#repository)
    - [Linux](#linux)
    - [Windows](#windows)

## Repository

### Linux

``` bash
STACK_NAME="<stack name>"
PROJECT_NAME="<project name>"
REGION="<region code>"

### Repository Configuration - General
RepositoryName=""   # [REQUIRED] The name of ECR repository.

### Repository Configuration - Encryption
EncryptionType=""   # [REQUIRED] The type of ECR repository encryption.
KmsKey=""           # [optional] The alias, ID, or ARN of KMS key for ECR repository encryption.

### Repository Configuration - Scanning
Scanning=""         # [REQUIRED] Enable or disable image scanning.

### Repository Configuration - Immutable
Immutable=""        # [REQUIRED] Mutable of immutable ECR repository's images.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/ecr/repository.yaml

# Using `deploy`
aws cloudformation deploy \
    --template-file ./repository.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        RepositoryName=$RepositoryName \
        EncryptionType=$EncryptionType \
        KmsKey=$KmsKey \
        Scanning=$Scanning \
        Immutable=$Immutable \
    --disable-rollback \
    --tags project=$PROJECT_NAME \
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack \
    --template-body file://repository.yaml \
    --stack-name $STACK_NAME \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME \
        ParameterKey=RepositoryName,ParameterValue=$RepositoryName \
        ParameterKey=EncryptionType,ParameterValue=$EncryptionType \
        ParameterKey=KmsKey,ParameterValue=$KmsKey \
        ParameterKey=Scanning,ParameterValue=$Scanning \
        ParameterKey=Immutable,ParameterValue=$Immutable \
    --disable-rollback \
    --tags Key=project,Value=$PROJECT_NAME \
    --region $REGION
```

### Windows

``` powershell
$STACK_NAME="<stack name>"
$PROJECT_NAME="<project name>"
$REGION="<region code>"

### Repository Configuration - General
$RepositoryName=""  # [REQUIRED] The name of ECR repository.

### Repository Configuration - Encryption
$EncryptionType=""  # [REQUIRED] The type of ECR repository encryption.
$KmsKey=""          # [optional] The alias, ID, or ARN of KMS key for ECR repository encryption.

### Repository Configuration - Scanning
$Scanning=""        # [REQUIRED] Enable or disable image scanning.

### Repository Configuration - Immutable
$Immutable=""       # [REQUIRED] Mutable of immutable ECR repository's images.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/ecr/repository.yaml

# Using `deploy`
aws cloudformation deploy `
    --template-file ./repository.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        RepositoryName=$RepositoryName `
        EncryptionType=$EncryptionType `
        KmsKey=$KmsKey `
        Scanning=$Scanning `
        Immutable=$Immutable `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack `
    --template-body file://repository.yaml `
    --stack-name $STACK_NAME `
    --parameters `
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME `
        ParameterKey=RepositoryName,ParameterValue=$RepositoryName `
        ParameterKey=EncryptionType,ParameterValue=$EncryptionType `
        ParameterKey=KmsKey,ParameterValue=$KmsKey `
        ParameterKey=Scanning,ParameterValue=$Scanning `
        ParameterKey=Immutable,ParameterValue=$Immutable `
    --disable-rollback `
    --tags Key=project,Value=$PROJECT_NAME `
    --region $REGION
```