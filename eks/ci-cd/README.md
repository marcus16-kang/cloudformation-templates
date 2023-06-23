# EKS CI/CD with AWS Development Tools

- [EKS CI/CD with AWS Development Tools](#eks-cicd-with-aws-development-tools)
  - [Artifact](#artifact)
    - [Linux](#linux)
    - [Windows](#windows)
  - [CodeCommit](#codecommit)
    - [Linux](#linux-1)
    - [Windows](#windows-1)
  - [CodeBuild - Build](#codebuild---build)
    - [Linux](#linux-2)
    - [Windows](#windows-2)
  - [CodeBuild - Deploy](#codebuild---deploy)
    - [Linux](#linux-3)
    - [Windows](#windows-3)
  - [CodePipeline](#codepipeline)
    - [Linux](#linux-4)
    - [Windows](#windows-4)

## [Artifact](artifact.yaml)

### Linux

``` bash
STACK_NAME=""
PROJECT_NAME=""
REGION=""

### Artifact Configuration - Bucket
ArtifactBucketName=""                    # [REQUIRED] The name of artifact S3 bucket.
ArtifactEncryptionKeyId="alias/aws/s3"   # [optional] The key ARN, id, alias ARN, or name to encrypt artifact S3 bucket. (Default is alias/aws/s3)

### Artifact Configuration - Logging
ArtifactLoggingDestinationBucketName=""  # [optional] The bucket name of artifact S3 bucket logging destination.
ArtifactLoggingDestinationPrefix=""      # [optional] The log prefix of artifact S3 bucket logging.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/ci-cd/artifact.yaml

# Using `deploy`
aws cloudformation deploy \
    --template-file ./artifact.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        ArtifactBucketName=$ArtifactBucketName \
        ArtifactEncryptionKeyId=$ArtifactEncryptionKeyId \
        ArtifactLoggingDestinationBucketName=$ArtifactLoggingDestinationBucketName \
        ArtifactLoggingDestinationPrefix=$ArtifactLoggingDestinationPrefix \
    --disable-rollback \
    --tags project=$PROJECT_NAME \
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack \
    --template-body file://artifact.yaml \
    --stack-name $STACK_NAME \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME \
        ParameterKey=ArtifactBucketName,ParameterValue=$ArtifactBucketName \
        ParameterKey=ArtifactEncryptionKeyId,ParameterValue=$ArtifactEncryptionKeyId \
        ParameterKey=ArtifactLoggingDestinationBucketName,ParameterValue=$ArtifactLoggingDestinationBucketName \
        ParameterKey=ArtifactLoggingDestinationPrefix,ParameterValue=$ArtifactLoggingDestinationPrefix \
    --disable-rollback \
    --tags Key=project,Value=$PROJECT_NAME \
    --region $REGION
```

### Windows

``` bash
$STACK_NAME=""
$PROJECT_NAME=""
$REGION=""

### Artifact Configuration - Bucket
$ArtifactBucketName=""                   # [REQUIRED] The name of artifact S3 bucket.
$ArtifactEncryptionKeyId="alias/aws/s3"  # [optional] The key ARN, id, alias ARN, or name to encrypt artifact S3 bucket. (Default is alias/aws/s3)


### Artifact Configuration - Logging
$ArtifactLoggingDestinationBucketName="" # [optional] The bucket name of artifact S3 bucket logging destination.
$ArtifactLoggingDestinationPrefix=""     # [optional] The log prefix of artifact S3 bucket logging.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/ci-cd/artifact.yaml

# Using `deploy`
aws cloudformation deploy `
    --template-file ./artifact.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        ArtifactBucketName=$ArtifactBucketName `
        ArtifactEncryptionKeyId=$ArtifactEncryptionKeyId `
        ArtifactLoggingDestinationBucketName=$ArtifactLoggingDestinationBucketName `
        ArtifactLoggingDestinationPrefix=$ArtifactLoggingDestinationPrefix `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack `
    --template-body file://artifact.yaml `
    --stack-name $STACK_NAME `
    --parameters `
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME `
        ParameterKey=ArtifactBucketName,ParameterValue=$ArtifactBucketName `
        ParameterKey=ArtifactEncryptionKeyId,ParameterValue=$ArtifactEncryptionKeyId `
        ParameterKey=ArtifactLoggingDestinationBucketName,ParameterValue=$ArtifactLoggingDestinationBucketName `
        ParameterKey=ArtifactLoggingDestinationPrefix,ParameterValue=$ArtifactLoggingDestinationPrefix `
    --disable-rollback `
    --tags Key=project,Value=$PROJECT_NAME `
    --region $REGION
```

## [CodeCommit](codecommit.yaml)

### Linux

``` bash
STACK_NAME=""
PROJECT_NAME=""
REGION=""

RepositoryName=""                   # [REQUIRED] The Id of EKS Cluster Security Group.
EnableNotification=""               # (`enable` or `disable`) [optional] Enable of disable CodeCommit's event notification.
NotificationTopicName=""            # [optional] The name of SNS topic for CodeCommit event notification
NotificationTopicEncryptionKey=""   # [optional] The key ID, ARN, alias name, or arn of SNS topic encryption.


curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/ci-cd/codecommit.yaml

# Using `deploy`
aws cloudformation deploy \
    --stack-name $STACK_NAME \
    --template-file ./codecommit.yaml \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        RepositoryName=$RepositoryName \
        EnableNotification=$EnableNotification \
        NotificationTopicName=$NotificationTopicName \
        NotificationTopicEncryptionKey=$NotificationTopicEncryptionKey \
    --tags project=$PROJECT_NAME \
    --region $REGION \
    --disable-rollback

# Using `create-stack`
aws cloudformation create-stack \
    --stack-name $STACK_NAME \
    --template-body file://codecommit.yaml \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME \
        ParameterKey=RepositoryName,ParameterValue=$RepositoryName \
        ParameterKey=EnableNotification,ParameterValue=$EnableNotification \
        ParameterKey=NotificationTopicName,ParameterValue=$NotificationTopicName \
        ParameterKey=NotificationTopicEncryptionKey,ParameterValue=$NotificationTopicEncryptionKey \
    --tags Key=project,Value=$PROJECT_NAME \
    --region $REGION \
    --disable-rollback
```

### Windows

``` powershell
$STACK_NAME=""
$PROJECT_NAME=""
$REGION=""

$RepositoryName=""                  # [REQUIRED] The Id of EKS Cluster Security Group.
$EnableNotification=""              # (`enable` or `disable`) [optional] Enable of disable CodeCommit's event notification.
$NotificationTopicName=""           # [optional] The name of SNS topic for CodeCommit event notification
$NotificationTopicEncryptionKey=""  # [optional] The key ID, ARN, alias name, or arn of SNS topic encryption.


curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/ci-cd/codecommit.yaml

# Using `deploy`
aws cloudformation deploy `
    --stack-name $STACK_NAME `
    --template-file ./codecommit.yaml `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        RepositoryName=$RepositoryName `
        EnableNotification=$EnableNotification `
        NotificationTopicName=$NotificationTopicName `
        NotificationTopicEncryptionKey=$NotificationTopicEncryptionKey `
    --tags project=$PROJECT_NAME `
    --region $REGION `
    --disable-rollback

# Using `create-stack`
aws cloudformation create-stack `
    --stack-name $STACK_NAME `
    --template-body file://codecommit.yaml `
    --parameters `
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME `
        ParameterKey=RepositoryName,ParameterValue=$RepositoryName `
        ParameterKey=EnableNotification,ParameterValue=$EnableNotification `
        ParameterKey=NotificationTopicName,ParameterValue=$NotificationTopicName `
        ParameterKey=NotificationTopicEncryptionKey,ParameterValue=$NotificationTopicEncryptionKey `
    --tags Key=project,Value=$PROJECT_NAME `
    --region $REGION `
    --disable-rollback
```

---

## [CodeBuild - Build](codebuild-build.yaml)

### Linux

``` bash
STACK_NAME=""
PROJECT_NAME=""
REGION=""

### CodeCommit Configuration
CodeCommitStackName=""              # [REQUIRED] [REQUIRED] The name of CodeCommit stack.

### CodeBuild Configuration - General
BuildProjectName=""                 # [REQUIRED] The name of CodeBuild project.
ServiceRoleName=""                  # [REQUIRED] The name of CodeBuild service IAM role.
EncryptionKey="alias/aws/s3"        # [optional] The ARN or Alias of KMS key for encrypt artifacts. (Default is alias/aws/s3.)
ComputeType="BUILD_GENERAL1_SMALL"  # [optional] The type of CodeBuild compute type. (The ARM container DOES NOT SUPPORT 'BUILD_GENERAL1_MEDIUM'.)
# BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE
Image=""                            # [REQUIRED] The image tag of CodeBuild image.
# aws/codebuild/amazonlinux2-x86_64-standard:4.0 | aws/codebuild/amazonlinux2-x86_64-standard:5.0 | aws/codebuild/amazonlinux2-aarch64-standard:2.0 | aws/codebuild/amazonlinux2-aarch64-standard:3.0
ArchitectureType=""                 # [REQUIRED] The type of CodeBuild architecture type.
# LINUX_CONTAINER | ARM_CONTAINER
BuildSpecFileName="buildspec.yaml"  # [REQUIRED] The name of buildspec file for build image.

### CodeBuild Configuration - Artifact
ArtifactBucketName=""               # [REQUIRED] The name of artifact S3 bucket.
ArtifactBranchName="main"           # [REQUIRED] The name of artifact git branch.

### CodeBuild Configuration - Container
ImageRepositoryName=""              # [REQUIRED] The name of image repository.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/ci-cd/codebuild-build.yaml

# Using `deploy`
aws cloudformation deploy \
    --template-file ./codebuild-build.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        CodeCommitStackName=$CodeCommitStackName \
        BuildProjectName=$BuildProjectName \
        ServiceRoleName=$ServiceRoleName \
        EncryptionKey=$EncryptionKey \
        ComputeType=$ComputeType \
        Image=$Image \
        ArchitectureType=$ArchitectureType \
        BuildSpecFileName=$BuildSpecFileName \
        ArtifactBucketName=$ArtifactBucketName \
        ArtifactBranchName=$ArtifactBranchName \
        ImageRepositoryName=$ImageRepositoryName \
    --disable-rollback \
    --tags project=$PROJECT_NAME \
    --capabilities CAPABILITY_NAMED_IAM \
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack \
    --template-body file://codebuild-build.yaml \
    --stack-name $STACK_NAME \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME \
        ParameterKey=CodeCommitStackName,ParameterValue=$CodeCommitStackName \
        ParameterKey=BuildProjectName,ParameterValue=$BuildProjectName \
        ParameterKey=ServiceRoleName,ParameterValue=$ServiceRoleName \
        ParameterKey=EncryptionKey,ParameterValue=$EncryptionKey \
        ParameterKey=ComputeType,ParameterValue=$ComputeType \
        ParameterKey=Image,ParameterValue=$Image \
        ParameterKey=ArchitectureType,ParameterValue=$ArchitectureType \
        ParameterKey=BuildSpecFileName,ParameterValue=$BuildSpecFileName \
        ParameterKey=ArtifactBucketName,ParameterValue=$ArtifactBucketName \
        ParameterKey=ArtifactBranchName,ParameterValue=$ArtifactBranchName \
        ParameterKey=ImageRepositoryName,ParameterValue=$ImageRepositoryName \
    --disable-rollback \
    --tags Key=project,Value=$PROJECT_NAME \
    --capabilities CAPABILITY_NAMED_IAM \
    --region $REGION
```

### Windows

``` powershell
$STACK_NAME=""
$PROJECT_NAME=""
$REGION=""

### CodeCommit Configuration
$CodeCommitStackName=""             # [REQUIRED] [REQUIRED] The name of CodeCommit stack.

### CodeBuild Configuration - General
$BuildProjectName=""                # [REQUIRED] The name of CodeBuild project.
$ServiceRoleName=""                 # [REQUIRED] The name of CodeBuild service IAM role.
$EncryptionKey="alias/aws/s3"       # [optional] The ARN or Alias of KMS key for encrypt artifacts. (Default is alias/aws/s3.)
$ComputeType="BUILD_GENERAL1_SMALL" # [optional] The type of CodeBuild compute type. (The ARM container DOES NOT SUPPORT 'BUILD_GENERAL1_MEDIUM'.)
# BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE
$Image=""                           # [REQUIRED] The image tag of CodeBuild image.
# aws/codebuild/amazonlinux2-x86_64-standard:4.0 | aws/codebuild/amazonlinux2-x86_64-standard:5.0 | aws/codebuild/amazonlinux2-aarch64-standard:2.0 | aws/codebuild/amazonlinux2-aarch64-standard:3.0
$ArchitectureType=""                # [REQUIRED] The type of CodeBuild architecture type.
# LINUX_CONTAINER | ARM_CONTAINER
$BuildSpecFileName="buildspec.yaml" # [REQUIRED] The name of buildspec file for build image.

### CodeBuild Configuration - Artifact
$ArtifactBucketName=""              # [REQUIRED] The name of artifact S3 bucket.
$ArtifactBranchName="main"          # [REQUIRED] The name of artifact git branch.

### CodeBuild Configuration - Container
$ImageRepositoryName=""             # [REQUIRED] The name of image repository.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/ci-cd/codebuild-build.yaml

# Using `deploy`
aws cloudformation deploy `
    --template-file ./codebuild-build.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        CodeCommitStackName=$CodeCommitStackName `
        BuildProjectName=$BuildProjectName `
        ServiceRoleName=$ServiceRoleName `
        EncryptionKey=$EncryptionKey `
        ComputeType=$ComputeType `
        Image=$Image `
        ArchitectureType=$ArchitectureType `
        BuildSpecFileName=$BuildSpecFileName `
        ArtifactBucketName=$ArtifactBucketName `
        ArtifactBranchName=$ArtifactBranchName `
        ImageRepositoryName=$ImageRepositoryName `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack `
    --template-body file://codebuild-build.yaml `
    --stack-name $STACK_NAME `
    --parameters `
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME `
        ParameterKey=CodeCommitStackName,ParameterValue=$CodeCommitStackName `
        ParameterKey=BuildProjectName,ParameterValue=$BuildProjectName `
        ParameterKey=ServiceRoleName,ParameterValue=$ServiceRoleName `
        ParameterKey=EncryptionKey,ParameterValue=$EncryptionKey `
        ParameterKey=ComputeType,ParameterValue=$ComputeType `
        ParameterKey=Image,ParameterValue=$Image `
        ParameterKey=ArchitectureType,ParameterValue=$ArchitectureType `
        ParameterKey=BuildSpecFileName,ParameterValue=$BuildSpecFileName `
        ParameterKey=ArtifactBucketName,ParameterValue=$ArtifactBucketName `
        ParameterKey=ArtifactBranchName,ParameterValue=$ArtifactBranchName `
        ParameterKey=ImageRepositoryName,ParameterValue=$ImageRepositoryName `
    --disable-rollback `
    --tags Key=project,Value=$PROJECT_NAME `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION
```

---

## [CodeBuild - Deploy](codebuild-deploy.yaml)

### Linux

``` bash
STACK_NAME=""
PROJECT_NAME=""
REGION=""

### CodeCommit Configuration
CodeCommitStackName=""                  # [REQUIRED] The name of CodeCommit stack.

### CodeBuild Configuration - General
BuildProjectName=""                     # [REQUIRED] The name of CodeBuild project.
ServiceRoleName=""                      # [REQUIRED] The name of CodeBuild service IAM role.
EncryptionKey="alias/aws/s3"            # [optional] The ARN or Alias of KMS key for encrypt artifacts. (Default is alias/aws/s3.)
ComputeType="BUILD_GENERAL1_SMALL"      # [optional] The type of CodeBuild compute type. (The ARM container DOES NOT SUPPORT 'BUILD_GENERAL1_MEDIUM'.)
# BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE
Image=""                                # [REQUIRED] The image tag of CodeBuild image.
# aws/codebuild/amazonlinux2-x86_64-standard:4.0 | aws/codebuild/amazonlinux2-x86_64-standard:5.0 | aws/codebuild/amazonlinux2-aarch64-standard:2.0 | aws/codebuild/amazonlinux2-aarch64-standard:3.0
ArchitectureType=""                     # [REQUIRED] The type of CodeBuild architecture type.
# LINUX_CONTAINER | ARM_CONTAINER
DeploySpecFileName="deployspec.yaml"    # [REQUIRED] The name of buildspec file for deploy image.

### CodeBuild Configuration - Artifact
ArtifactBucketName=""                   # [REQUIRED] The name of artifact S3 bucket.
ArtifactBranchName="main"               # [REQUIRED] The name of artifact git branch.

### CodeBuild Configuration - VPC
VpcId=""                                # [REQUIRED] The ID of VPC for the CodeBuild.
Subnets=""                              # [REQUIRED] The list of subnets id for the CodeBuild.
SecurityGroupId=""                      # [REQUIRED] The ID of security Group for the CodeBuild.

### Kubernetes Configuration
ClusterName=""                          # [REQUIRED] The name of EKS cluster.
NamespaceName=""                        # [REQUIRED] The name of Kubernetes Namespace.
DeploymentName=""                       # [REQUIRED] The name of Kubernetes Deployment.
ContainerName=""                        # [REQUIRED] The name of container in Kubernetes Deployment.
ImageRepositoryName=""                  # [REQUIRED] The name of image repository.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/ci-cd/codebuild-deploy.yaml

# Using `deploy`
aws cloudformation deploy \
    --template-file ./codebuild-deploy.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        CodeCommitStackName=$CodeCommitStackName \
        BuildProjectName=$BuildProjectName \
        ServiceRoleName=$ServiceRoleName \
        EncryptionKey=$EncryptionKey \
        ComputeType=$ComputeType \
        Image=$Image \
        ArchitectureType=$ArchitectureType \
        BuildSpecFileName=$BuildSpecFileName \
        ArtifactBucketName=$ArtifactBucketName \
        ArtifactBranchName=$ArtifactBranchName \
        VpcId=$VpcId \
        Subnets=$Subnets \
        SecurityGroupId=$SecurityGroupId \
        ClusterName=$ClusterName \
        NamespaceName=$NamespaceName \
        DeploymentName=$DeploymentName \
        ContainerName=$ContainerName \
        ImageRepositoryName=$ImageRepositoryName \
    --disable-rollback \
    --tags project=$PROJECT_NAME \
    --capabilities CAPABILITY_NAMED_IAM \
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack \
    --template-body file://codebuild-deploy.yaml \
    --stack-name $STACK_NAME \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME \
        ParameterKey=CodeCommitStackName,ParameterValue=$CodeCommitStackName \
        ParameterKey=BuildProjectName,ParameterValue=$BuildProjectName \
        ParameterKey=ServiceRoleName,ParameterValue=$ServiceRoleName \
        ParameterKey=EncryptionKey,ParameterValue=$EncryptionKey \
        ParameterKey=ComputeType,ParameterValue=$ComputeType \
        ParameterKey=Image,ParameterValue=$Image \
        ParameterKey=ArchitectureType,ParameterValue=$ArchitectureType \
        ParameterKey=BuildSpecFileName,ParameterValue=$BuildSpecFileName \
        ParameterKey=ArtifactBucketName,ParameterValue=$ArtifactBucketName \
        ParameterKey=ArtifactBranchName,ParameterValue=$ArtifactBranchName \
        ParameterKey=VpcId,ParameterValue=$VpcId \
        ParameterKey=Subnets,ParameterValue=$Subnets \
        ParameterKey=SecurityGroupId,ParameterValue=$SecurityGroupId \
        ParameterKey=ClusterName,ParameterValue=$ClusterName \
        ParameterKey=NamespaceName,ParameterValue=$NamespaceName \
        ParameterKey=DeploymentName,ParameterValue=$DeploymentName \
        ParameterKey=ContainerName,ParameterValue=$ContainerName \
        ParameterKey=ImageRepositoryName,ParameterValue=$ImageRepositoryName \
    --disable-rollback \
    --tags Key=project,Value=$PROJECT_NAME \
    --capabilities CAPABILITY_NAMED_IAM \
    --region $REGION
```

### Windows

``` bash
$STACK_NAME=""
$PROJECT_NAME=""
$REGION=""

### CodeCommit Configuration
$CodeCommitStackName=""                 # [REQUIRED] The name of CodeCommit stack.

### CodeBuild Configuration - General
$BuildProjectName=""                    # [REQUIRED] The name of CodeBuild project.
$ServiceRoleName=""                     # [REQUIRED] The name of CodeBuild service IAM role.
$EncryptionKey="alias/aws/s3"           # [optional] The ARN or Alias of KMS key for encrypt artifacts. (Default is alias/aws/s3.)
$ComputeType="BUILD_GENERAL1_SMALL"     # [optional] The type of CodeBuild compute type. (The ARM container DOES NOT SUPPORT 'BUILD_GENERAL1_MEDIUM'.)
# BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE
$Image=""                               # [REQUIRED] The image tag of CodeBuild image.
# aws/codebuild/amazonlinux2-x86_64-standard:4.0 | aws/codebuild/amazonlinux2-x86_64-standard:5.0 | aws/codebuild/amazonlinux2-aarch64-standard:2.0 | aws/codebuild/amazonlinux2-aarch64-standard:3.0
$ArchitectureType=""                    # [REQUIRED] The type of CodeBuild architecture type.
# LINUX_CONTAINER | ARM_CONTAINER
$DeploySpecFileName="deployspec.yaml"   # [REQUIRED] The name of buildspec file for deploy image.

### CodeBuild Configuration - Artifact
$ArtifactBucketName=""                  # [REQUIRED] The name of artifact S3 bucket.
$ArtifactBranchName="main"              # [REQUIRED] The name of artifact git branch.

### CodeBuild Configuration - VPC
$VpcId=""                               # [REQUIRED] The ID of VPC for the CodeBuild.
$Subnets=""                             # [REQUIRED] The list of subnets id for the CodeBuild.
$SecurityGroupId=""                     # [REQUIRED] The ID of security Group for the CodeBuild.

### Kubernetes Configuration
$ClusterName=""                         # [REQUIRED] The name of EKS cluster.
$NamespaceName=""                       # [REQUIRED] The name of Kubernetes Namespace.
$DeploymentName=""                      # [REQUIRED] The name of Kubernetes Deployment.
$ContainerName=""                       # [REQUIRED] The name of container in Kubernetes Deployment.
$ImageRepositoryName=""                 # [REQUIRED] The name of image repository.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/ci-cd/codebuild-deploy.yaml

# Using `deploy`
aws cloudformation deploy `
    --template-file ./codebuild-deploy.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        CodeCommitStackName=$CodeCommitStackName `
        BuildProjectName=$BuildProjectName `
        ServiceRoleName=$ServiceRoleName `
        EncryptionKey=$EncryptionKey `
        ComputeType=$ComputeType `
        Image=$Image `
        ArchitectureType=$ArchitectureType `
        BuildSpecFileName=$BuildSpecFileName `
        ArtifactBucketName=$ArtifactBucketName `
        ArtifactBranchName=$ArtifactBranchName `
        VpcId=$VpcId `
        Subnets=$Subnets `
        SecurityGroupId=$SecurityGroupId `
        ClusterName=$ClusterName `
        NamespaceName=$NamespaceName `
        DeploymentName=$DeploymentName `
        ContainerName=$ContainerName `
        ImageRepositoryName=$ImageRepositoryName `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack `
    --template-file ./codebuild-deploy.yaml `
    --stack-name $STACK_NAME `
    --parameters `
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME `
        ParameterKey=CodeCommitStackName,ParameterValue=$CodeCommitStackName `
        ParameterKey=BuildProjectName,ParameterValue=$BuildProjectName `
        ParameterKey=ServiceRoleName,ParameterValue=$ServiceRoleName `
        ParameterKey=EncryptionKey,ParameterValue=$EncryptionKey `
        ParameterKey=ComputeType,ParameterValue=$ComputeType `
        ParameterKey=Image,ParameterValue=$Image `
        ParameterKey=ArchitectureType,ParameterValue=$ArchitectureType `
        ParameterKey=BuildSpecFileName,ParameterValue=$BuildSpecFileName `
        ParameterKey=ArtifactBucketName,ParameterValue=$ArtifactBucketName `
        ParameterKey=ArtifactBranchName,ParameterValue=$ArtifactBranchName `
        ParameterKey=VpcId,ParameterValue=$VpcId `
        ParameterKey=Subnets,ParameterValue=$Subnets `
        ParameterKey=SecurityGroupId,ParameterValue=$SecurityGroupId `
        ParameterKey=ClusterName,ParameterValue=$ClusterName `
        ParameterKey=NamespaceName,ParameterValue=$NamespaceName `
        ParameterKey=DeploymentName,ParameterValue=$DeploymentName `
        ParameterKey=ContainerName,ParameterValue=$ContainerName `
        ParameterKey=ImageRepositoryName,ParameterValue=$ImageRepositoryName `
    --disable-rollback `
    --tags Key=project,Value=$PROJECT_NAME `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION
```

---

## [CodePipeline](codepipeline.yaml)

### Linux

``` bash
STACK_NAME=""
PROJECT_NAME=""
REGION=""

### CodeCommit Configuration
CodeCommitStackName=""                   # [REQUIRED] The name of CodeCommit stack.
CodeCommitBranchName="main"              # [REQUIRED] The name of CodeCommit branch name for trigger pipeline.

### CodeBuild (Build Image) Configuration
CodeBuildStackName=""                    # [REQUIRED] The name of CodeBuild (build image) stack.

### CodeBuild (Deploy Image) Configuration
CodeBuildDeployStackName=""              # [REQUIRED] The name of CodeBuild (deploy image) stack.

### CodePipeline Configuration - Pipeline
PipelineName=""                          # [REQUIRED] the name of CodePipeline pipeline.
ServiceRoleName=""                       # [REQUIRED] The name of CodePipeline service IAM role.

### CodePipeline Configuration - Artifact Bucket
ArtifactBucketName=""                    # [REQUIRED] The name of artifact S3 bucket.
ArtifactEncryptionKeyId="alias/aws/s3"   # [optional] The key ARN, id, alias ARN, or name to encrypt artifact S3 bucket. (Default is alias/aws/s3)

### CodePipeline Configuration - EventBridge
EventBridgeRoleName=""                   # [optional] The name of EventBridge IAM role.
EventBridgeRuleName=""                   # [optional] The name of EventBridge rule name.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/ci-cd/codepipeline.yaml

# Using `deploy`
aws cloudformation deploy \
    --template-file ./codepipeline.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        CodeCommitStackName=$CodeCommitStackName \
        CodeCommitBranchName=$CodeCommitBranchName \
        CodeBuildStackName=$CodeBuildStackName \
        CodeBuildDeployStackName=$CodeBuildDeployStackName \
        PipelineName=$PipelineName \
        ServiceRoleName=$ServiceRoleName \
        ArtifactBucketName=$ArtifactBucketName \
        ArtifactEncryptionKeyId=$ArtifactEncryptionKeyId \
        EventBridgeRoleName=$EventBridgeRoleName \
        EventBridgeRuleName=$EventBridgeRuleName \
    --disable-rollback \
    --tags project=$PROJECT_NAME \
    --capabilities CAPABILITY_NAMED_IAM \
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack \
    --template-body file://codepipeline.yaml \
    --stack-name $STACK_NAME \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME \
        ParameterKey=CodeCommitStackName,ParameterValue=$CodeCommitStackName \
        ParameterKey=CodeCommitBranchName,ParameterValue=$CodeCommitBranchName \
        ParameterKey=CodeBuildStackName,ParameterValue=$CodeBuildStackName \
        ParameterKey=CodeBuildDeployStackName,ParameterValue=$CodeBuildDeployStackName \
        ParameterKey=PipelineName,ParameterValue=$PipelineName \
        ParameterKey=ServiceRoleName,ParameterValue=$ServiceRoleName \
        ParameterKey=ArtifactBucketName,ParameterValue=$ArtifactBucketName \
        ParameterKey=ArtifactEncryptionKeyId,ParameterValue=$ArtifactEncryptionKeyId \
        ParameterKey=EventBridgeRoleName,ParameterValue=$EventBridgeRoleName \
        ParameterKey=EventBridgeRuleName,ParameterValue=$EventBridgeRuleName \
    --disable-rollback \
    --tags Key=project,Value=$PROJECT_NAME \
    --capabilities CAPABILITY_NAMED_IAM \
    --region $REGION
```

### Windows

``` bash
$STACK_NAME=""
$PROJECT_NAME=""
$REGION=""

### CodeCommit Configuration
$CodeCommitStackName=""                  # [REQUIRED] The name of CodeCommit stack.
$CodeCommitBranchName="main"             # [REQUIRED] The name of CodeCommit branch name for trigger pipeline.

### CodeBuild (Build Image) Configuration
$CodeBuildStackName=""                   # [REQUIRED] The name of CodeBuild (build image) stack.

### CodeBuild (Deploy Image) Configuration
$CodeBuildDeployStackName=""             # [REQUIRED] The name of CodeBuild (deploy image) stack.

### CodePipeline Configuration - Pipeline
$PipelineName=""                         # [REQUIRED] the name of CodePipeline pipeline.
$ServiceRoleName=""                      # [REQUIRED] The name of CodePipeline service IAM role.

### CodePipeline Configuration - Artifact Bucket
$ArtifactBucketName=""                   # [REQUIRED] The name of artifact S3 bucket.
$ArtifactEncryptionKeyId="alias/aws/s3"  # [optional] The key ARN, id, alias ARN, or name to encrypt artifact S3 bucket. (Default is alias/aws/s3)

### CodePipeline Configuration - EventBridge
$EventBridgeRoleName=""                  # [optional] The name of EventBridge IAM role.
$EventBridgeRuleName=""                  # [optional] The name of EventBridge rule name.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/ci-cd/codepipeline.yaml

# Using `deploy`
aws cloudformation deploy `
    --template-file ./codepipeline.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        CodeCommitStackName=$CodeCommitStackName `
        CodeCommitBranchName=$CodeCommitBranchName `
        CodeBuildStackName=$CodeBuildStackName `
        CodeBuildDeployStackName=$CodeBuildDeployStackName `
        PipelineName=$PipelineName `
        ServiceRoleName=$ServiceRoleName `
        ArtifactBucketName=$ArtifactBucketName `
        ArtifactEncryptionKeyId=$ArtifactEncryptionKeyId `
        EventBridgeRoleName=$EventBridgeRoleName `
        EventBridgeRuleName=$EventBridgeRuleName `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION

# Using `create-stack`
aws cloudformation create-stack `
    --template-body file://codepipeline.yaml `
    --stack-name $STACK_NAME `
    --parameters `
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME `
        ParameterKey=CodeCommitStackName,ParameterValue=$CodeCommitStackName `
        ParameterKey=CodeCommitBranchName,ParameterValue=$CodeCommitBranchName `
        ParameterKey=CodeBuildStackName,ParameterValue=$CodeBuildStackName `
        ParameterKey=CodeBuildDeployStackName,ParameterValue=$CodeBuildDeployStackName `
        ParameterKey=PipelineName,ParameterValue=$PipelineName `
        ParameterKey=ServiceRoleName,ParameterValue=$ServiceRoleName `
        ParameterKey=ArtifactBucketName,ParameterValue=$ArtifactBucketName `
        ParameterKey=ArtifactEncryptionKeyId,ParameterValue=$ArtifactEncryptionKeyId `
        ParameterKey=EventBridgeRoleName,ParameterValue=$EventBridgeRoleName `
        ParameterKey=EventBridgeRuleName,ParameterValue=$EventBridgeRuleName `
    --disable-rollback `
    --tags Key=project,Value=$PROJECT_NAME `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $REGION
```