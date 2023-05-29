# ECS Blue-Green CI/CD

- [ECS Blue-Green CI/CD](#ecs-blue-green-cicd)
  - [CodeCommit](#codecommit)
    - [Note](#note)
    - [Linux](#linux)
    - [Windows](#windows)
  - [CodeBuild](#codebuild)
    - [Linux](#linux-1)
    - [Windows](#windows-1)
  - [CodeDeploy](#codedeploy)
    - [Linux](#linux-2)
    - [Windows](#windows-2)
  - [CodePipeline](#codepipeline)
    - [Linux](#linux-3)
    - [Windows](#windows-3)

## CodeCommit

### Note

If you want to encrypt SNS topic server-side encryption, you should add this policy to KMS resource-based policy.

``` json
{
    "Effect": "Allow",
    "Principal": {
        "Service": "codestar-notifications.amazonaws.com"
    },
    "Action": [
        "kms:GenerateDataKey*",
        "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "sns.<REGION>.amazonaws.com"
        }
    }
}
```

### Linux

``` bash
STACK_NAME="<cloudformation stack name>"
PROJECT_NAME="<project name>"
REGION="<region code>"

### CodeCommit Configuration - General
RepositoryName=""                   # [REQUIRED] The name of CodeCommit repository.

### CodeCommit Configuration - Notification
EnableNotification="enable"         # `enable`(default) of `disable` | [REQUIRED] Enable of disable CodeCommit's event notification.
NotificationTopicName=""            # [optional] The name of SNS topic for CodeCommit event notification
NotificationTopicEncryptionKey=""   # [optional] The key ID, ARN, alias name, or arn of SNS topic encryption.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/ecs/ci-cd/blue-green/codecommit.yaml

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
$STACK_NAME="<cloudformation stack name>"
$PROJECT_NAME="<project name>"
$REGION="<region code>"

### CodeCommit Configuration - General
$RepositoryName=""                  # [REQUIRED] The name of CodeCommit repository.

### CodeCommit Configuration - Notification
$EnableNotification="enable"        # `enable`(default) of `disable` | [REQUIRED] Enable of disable CodeCommit's event notification.
$NotificationTopicName=""           # [optional] The name of SNS topic for CodeCommit event notification
$NotificationTopicEncryptionKey=""  # [optional] The key ID, ARN, alias name, or arn of SNS topic encryption.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/ecs/ci-cd/blue-green/codecommit.yaml

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

## CodeBuild

### Linux

``` bash
STACK_NAME="<cloudformation stack name>"
PROJECT_NAME="<project name>"
REGION="<region code>"

### CodeCommit Configuration
CodeCommitStackName=""              # [REQUIRED] The name of CodeCommit stack.

### CodeBuild Configuration - General
BuildProjectName=""                 # [REQUIRED] The name of CodeBuild project.
ServiceRoleName=""                  # [REQUIRED] The name of CodeBuild service IAM role.
EncryptionKey="alias/aws/s3"        # [optional] The ARN or Alias of KMS key for encrypt artifacts. (Default is alias/aws/s3.)
ComputeType="BUILD_GENERAL1_SMALL"  # [optional] The type of CodeBuild compute type. (The ARM container DOES NOT SUPPORT 'BUILD_GENERAL1_MEDIUM'.)
# BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE
Image=""                            # [REQUIRED] The image tag of CodeBuild image.
# aws/codebuild/amazonlinux2-x86_64-standard:3.0 | aws/codebuild/amazonlinux2-x86_64-standard:4.0 | aws/codebuild/amazonlinux2-aarch64-standard:1.0 | aws/codebuild/amazonlinux2-aarch64-standard:2.0
ArchitectureType=""                 # `LINUX_CONTAINER` or `ARM_CONTAINER` | [REQUIRED] The type of CodeBuild architecture type.
ArtifactBucketName=""               # [REQUIRED] The name of artifact S3 bucket.
ArtifactBranchName="main"           # [REQUIRED] The name of artifact git branch.

### CodeBuild Configuration - Container
ImageRepositoryName=""              # [REQUIRED] The name of image repository.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/ecs/ci-cd/blue-green/codebuild.yaml

# Using `deploy`
aws cloudformation deploy \
    --stack-name $STACK_NAME \
    --template-file ./codebuild.yaml \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        CodeCommitStackName=$CodeCommitStackName \
        BuildProjectName=$BuildProjectName \
        ServiceRoleName=$ServiceRoleName \
        EncryptionKey=$EncryptionKey \
        ComputeType=$ComputeType \
        Image=$Image \
        ArchitectureType=$ArchitectureType \
        ArtifactBucketName=$ArtifactBucketName \
        ArtifactBranchName=$ArtifactBranchName \
        ImageRepositoryName=$ImageRepositoryName \
    --tags project=$PROJECT_NAME \
    --region $REGION \
    --disable-rollback

# Using `create-stack`
aws cloudformation create-stack \
    --stack-name $STACK_NAME \
    --template-body file://codebuild.yaml \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME \
        ParameterKey=CodeCommitStackName,ParameterValue=$CodeCommitStackName \
        ParameterKey=BuildProjectName,ParameterValue=$BuildProjectName \
        ParameterKey=ServiceRoleName,ParameterValue=$ServiceRoleName \
        ParameterKey=EncryptionKey,ParameterValue=$EncryptionKey \
        ParameterKey=ComputeType,ParameterValue=$ComputeType \
        ParameterKey=Image,ParameterValue=$Image \
        ParameterKey=ArchitectureType,ParameterValue=$ArchitectureType \
        ParameterKey=ArtifactBucketName,ParameterValue=$ArtifactBucketName \
        ParameterKey=ArtifactBranchName,ParameterValue=$ArtifactBranchName \
        ParameterKey=ImageRepositoryName,ParameterValue=$ImageRepositoryName \
    --tags Key=project,Value=$PROJECT_NAME \
    --region $REGION \
    --disable-rollback
```

### Windows

``` powershell
$STACK_NAME="<cloudformation stack name>"
$PROJECT_NAME="<project name>"
$REGION="<region code>"

### CodeCommit Configuration
$CodeCommitStackName=""             # [REQUIRED] The name of CodeCommit stack.

### CodeBuild Configuration - General
$BuildProjectName=""                # [REQUIRED] The name of CodeBuild project.
$ServiceRoleName=""                 # [REQUIRED] The name of CodeBuild service IAM role.
$EncryptionKey="alias/aws/s3"       # [optional] The ARN or Alias of KMS key for encrypt artifacts. (Default is alias/aws/s3.)
$ComputeType="BUILD_GENERAL1_SMALL" # [optional] The type of CodeBuild compute type. (The ARM container DOES NOT SUPPORT 'BUILD_GENERAL1_MEDIUM'.)
# BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE
$Image=""                           # [REQUIRED] The image tag of CodeBuild image.
# aws/codebuild/amazonlinux2-x86_64-standard:3.0 | aws/codebuild/amazonlinux2-x86_64-standard:4.0 | aws/codebuild/amazonlinux2-aarch64-standard:1.0 | aws/codebuild/amazonlinux2-aarch64-standard:2.0
$ArchitectureType=""                # `LINUX_CONTAINER` or `ARM_CONTAINER` | [REQUIRED] The type of CodeBuild architecture type.
$ArtifactBucketName=""              # [REQUIRED] The name of artifact S3 bucket.
$ArtifactBranchName="main"          # [REQUIRED] The name of artifact git branch.

### CodeBuild Configuration - Container
$ImageRepositoryName=""             # [REQUIRED] The name of image repository.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/ecs/ci-cd/blue-green/codebuild.yaml

# Using `deploy`
aws cloudformation deploy `
    --stack-name $STACK_NAME `
    --template-file ./codebuild.yaml `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        CodeCommitStackName=$CodeCommitStackName `
        BuildProjectName=$BuildProjectName `
        ServiceRoleName=$ServiceRoleName `
        EncryptionKey=$EncryptionKey `
        ComputeType=$ComputeType `
        Image=$Image `
        ArchitectureType=$ArchitectureType `
        ArtifactBucketName=$ArtifactBucketName `
        ArtifactBranchName=$ArtifactBranchName `
        ImageRepositoryName=$ImageRepositoryName `
    --tags project=$PROJECT_NAME `
    --region $REGION `
    --disable-rollback

# Using `create-stack`
aws cloudformation create-stack `
    --stack-name $STACK_NAME `
    --template-body file://codebuild.yaml `
    --parameters `
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME `
        ParameterKey=CodeCommitStackName,ParameterValue=$CodeCommitStackName `
        ParameterKey=BuildProjectName,ParameterValue=$BuildProjectName `
        ParameterKey=ServiceRoleName,ParameterValue=$ServiceRoleName `
        ParameterKey=EncryptionKey,ParameterValue=$EncryptionKey `
        ParameterKey=ComputeType,ParameterValue=$ComputeType `
        ParameterKey=Image,ParameterValue=$Image `
        ParameterKey=ArchitectureType,ParameterValue=$ArchitectureType `
        ParameterKey=ArtifactBucketName,ParameterValue=$ArtifactBucketName `
        ParameterKey=ArtifactBranchName,ParameterValue=$ArtifactBranchName `
        ParameterKey=ImageRepositoryName,ParameterValue=$ImageRepositoryName `
    --tags Key=project,Value=$PROJECT_NAME `
    --region $REGION `
    --disable-rollback
```

## CodeDeploy

### Linux

``` bash
STACK_NAME="<cloudformation stack name>"
PROJECT_NAME="<project name>"
REGION="<region code>"

### CodeDeploy Configuration - Application
ApplicationName=""      # [REQUIRED] The name of CodeDeploy application.
ServiceRoleName=""      # [REQUIRED] The name of CodeDeploy service IAM role.

### CodeDeploy Configuration - Deployment Group
DeploymentGroupName=""  # [REQUIRED] The name of CodeDeploy deployment group.
EcsClusterName=""       # [REQUIRED] The name of ECS cluster for CodeDeploy deployment group.
EcsServiceName=""       # [REQUIRED] The name of ECS service for CodeDeploy deployment group.

### CodeDeploy Configuration - Load Balancer
AlbListenerArn=""       # [REQUIRED] The arn of ECS service's ALB listener.
AlbTestListenerArn=""   # [optional] The arn of ECS service's ALB test listener.
AlbTargetGroup1Name=""  # [REQUIRED] The name of ECS service's ALB target group 1.
AlbTargetGroup2Name=""  # [REQUIRED] The name of ECS service's ALB target group 2.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/ecs/ci-cd/blue-green/codedeploy.yaml

# Using `deploy`
aws cloudformation deploy \
    --stack-name $STACK_NAME \
    --template-file ./codedeploy.yaml \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        ApplicationName=$ApplicationName \
        ServiceRoleName=$ServiceRoleName \
        DeploymentGroupName=$DeploymentGroupName \
        EcsClusterName=$EcsClusterName \
        EcsServiceName=$EcsServiceName \
        AlbListenerArn=$AlbListenerArn \
        AlbTestListenerArn=$AlbTestListenerArn \
        AlbTargetGroup1Name=$AlbTargetGroup1Name \
        AlbTargetGroup2Name=$AlbTargetGroup2Name \
    --tags project=$PROJECT_NAME \
    --region $REGION \
    --disable-rollback

# Using `create-stack`
aws cloudformation create-stack \
    --stack-name $STACK_NAME \
    --template-body file://codedeploy.yaml \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME \
        ParameterKey=ApplicationName,ParameterValue=$ApplicationName \
        ParameterKey=ServiceRoleName,ParameterValue=$ServiceRoleName \
        ParameterKey=DeploymentGroupName,ParameterValue=$DeploymentGroupName \
        ParameterKey=EcsClusterName,ParameterValue=$EcsClusterName \
        ParameterKey=EcsServiceName,ParameterValue=$EcsServiceName \
        ParameterKey=AlbListenerArn,ParameterValue=$AlbListenerArn \
        ParameterKey=AlbTestListenerArn,ParameterValue=$AlbTestListenerArn \
        ParameterKey=AlbTargetGroup1Name,ParameterValue=$AlbTargetGroup1Name \
        ParameterKey=AlbTargetGroup2Name,ParameterValue=$AlbTargetGroup2Name \
    --tags Key=project,Value=$PROJECT_NAME \
    --region $REGION \
    --disable-rollback
```

### Windows

``` powershell
$STACK_NAME="<cloudformation stack name>"
$PROJECT_NAME="<project name>"
$REGION="<region code>"

### CodeDeploy Configuration - Application
$ApplicationName=""     # [REQUIRED] The name of CodeDeploy application.
$ServiceRoleName=""     # [REQUIRED] The name of CodeDeploy service IAM role.

### CodeDeploy Configuration - Deployment Group
$DeploymentGroupName="" # [REQUIRED] The name of CodeDeploy deployment group.
$EcsClusterName=""      # [REQUIRED] The name of ECS cluster for CodeDeploy deployment group.
$EcsServiceName=""      # [REQUIRED] The name of ECS service for CodeDeploy deployment group.

### CodeDeploy Configuration - Load Balancer
$AlbListenerArn=""      # [REQUIRED] The arn of ECS service's ALB listener.
$AlbTestListenerArn=""  # [optional] The arn of ECS service's ALB test listener.
$AlbTargetGroup1Name="" # [REQUIRED] The name of ECS service's ALB target group 1.
$AlbTargetGroup2Name="" # [REQUIRED] The name of ECS service's ALB target group 2.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/ecs/ci-cd/blue-green/codedeploy.yaml

# Using `deploy`
aws cloudformation deploy `
    --stack-name $STACK_NAME `
    --template-file ./codedeploy.yaml `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        ApplicationName=$ApplicationName `
        ServiceRoleName=$ServiceRoleName `
        DeploymentGroupName=$DeploymentGroupName `
        EcsClusterName=$EcsClusterName `
        EcsServiceName=$EcsServiceName `
        AlbListenerArn=$AlbListenerArn `
        AlbTestListenerArn=$AlbTestListenerArn `
        AlbTargetGroup1Name=$AlbTargetGroup1Name `
        AlbTargetGroup2Name=$AlbTargetGroup2Name `
    --tags project=$PROJECT_NAME `
    --region $REGION `
    --disable-rollback

# Using `create-stack`
aws cloudformation create-stack `
    --stack-name $STACK_NAME `
    --template-body file://codedeploy.yaml `
    --parameters `
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME `
        ParameterKey=ApplicationName,ParameterValue=$ApplicationName `
        ParameterKey=ServiceRoleName,ParameterValue=$ServiceRoleName `
        ParameterKey=DeploymentGroupName,ParameterValue=$DeploymentGroupName `
        ParameterKey=EcsClusterName,ParameterValue=$EcsClusterName `
        ParameterKey=EcsServiceName,ParameterValue=$EcsServiceName `
        ParameterKey=AlbListenerArn,ParameterValue=$AlbListenerArn `
        ParameterKey=AlbTestListenerArn,ParameterValue=$AlbTestListenerArn `
        ParameterKey=AlbTargetGroup1Name,ParameterValue=$AlbTargetGroup1Name `
        ParameterKey=AlbTargetGroup2Name,ParameterValue=$AlbTargetGroup2Name `
    --tags Key=project,Value=$PROJECT_NAME `
    --region $REGION `
    --disable-rollback
```

## CodePipeline

### Linux

``` bash
STACK_NAME="<cloudformation stack name>"
PROJECT_NAME="<project name>"
REGION="<region code>"

### CodeCommit Configuration
CodeCommitStackName=""                      # [optional] The name of CodeCommit stack. (If you don't type anything, pipeline doesn't create source stage.)
CodeCommitBranchName=""                     # [optional] The name of CodeCommit branch name for trigger pipeline.

### CodeBuild Configuration
CodeBuildStackName=""                       # [optional] The name of CodeBuild stack. (If you don't type anything, pipeline doesn't create build stage.)

### CodeDeploy Configuration
CodeDeployStackName=""                      # [optional] The name of CodeDeploy stack. (If you don't type anything, pipeline doesn't create deploy stage.)

### CodePipeline Configuration - Pipeline
PipelineName=""                             # [REQUIRED] the name of CodePipeline pipeline.
ServiceRoleName=""                          # [REQUIRED] The name of CodePipeline service IAM role.

### CodePipeline Configuration - Artifact Bucket
ArtifactBucketName=""                       # [REQUIRED] The name of artifact S3 bucket.
ArtifactEncryptionKeyId="alias/aws/s3"      # [optional] The key ARN, id, alias ARN, or name to encrypt artifact S3 bucket. (Default is alias/aws/s3)
ArtifactLoggingDestinationBucketName=""     # [optional] The bucket name of artifact S3 bucket logging destination.
ArtifactLoggingDestinationPrefix=""         # [optional] The log prefix of artifact S3 bucket logging.

### CodePipeline Configuration - Deploy
TaskDefinitionTemplatePath="taskdef.json"   # [optional] The file name of the task definition.
AppSpecTemplatePath="appspec.yaml"          # [optional] The file name of the appspec.

### CodePipeline Configuration - EventBridge
EventBridgeRoleName=""                      # [optional] The name of EventBridge IAM role.
EventBridgeRuleName=""                      # [optional] The name of EventBridge rule name.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/ecs/ci-cd/blue-green/codepipeline.yaml

# Using `deploy`
aws cloudformation deploy \
    --stack-name $STACK_NAME \
    --template-file ./codepipeline.yaml \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        CodeCommitStackName=$CodeCommitStackName \
        CodeCommitBranchName=$CodeCommitBranchName \
        CodeBuildStackName=$CodeBuildStackName \
        CodeDeployStackName=$CodeDeployStackName \
        PipelineName=$PipelineName \
        ServiceRoleName=$ServiceRoleName \
        ArtifactBucketName=$ArtifactBucketName \
        ArtifactEncryptionKeyId=$ArtifactEncryptionKeyId \
        ArtifactLoggingDestinationBucketName=$ArtifactLoggingDestinationBucketName \
        ArtifactLoggingDestinationPrefix=$ArtifactLoggingDestinationPrefix \
        TaskDefinitionTemplatePath=$TaskDefinitionTemplatePath \
        AppSpecTemplatePath=$AppSpecTemplatePath \
        EventBridgeRoleName=$EventBridgeRoleName \
        EventBridgeRuleName=$EventBridgeRuleName \
    --tags project=$PROJECT_NAME \
    --region $REGION \
    --disable-rollback

# Using `create-stack`
aws cloudformation create-stack \
    --stack-name $STACK_NAME \
    --template-body file://codepipeline.yaml \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME \
        ParameterKey=CodeCommitStackName,ParameterValue=$CodeCommitStackName \
        ParameterKey=CodeCommitBranchName,ParameterValue=$CodeCommitBranchName \
        ParameterKey=CodeBuildStackName,ParameterValue=$CodeBuildStackName \
        ParameterKey=CodeDeployStackName,ParameterValue=$CodeDeployStackName \
        ParameterKey=PipelineName,ParameterValue=$PipelineName \
        ParameterKey=ServiceRoleName,ParameterValue=$ServiceRoleName \
        ParameterKey=ArtifactBucketName,ParameterValue=$ArtifactBucketName \
        ParameterKey=ArtifactEncryptionKeyId,ParameterValue=$ArtifactEncryptionKeyId \
        ParameterKey=ArtifactLoggingDestinationBucketName,ParameterValue=$ArtifactLoggingDestinationBucketName \
        ParameterKey=ArtifactLoggingDestinationPrefix,ParameterValue=$ArtifactLoggingDestinationPrefix \
        ParameterKey=TaskDefinitionTemplatePath,ParameterValue=$TaskDefinitionTemplatePath \
        ParameterKey=AppSpecTemplatePath,ParameterValue=$AppSpecTemplatePath \
        ParameterKey=EventBridgeRoleName,ParameterValue=$EventBridgeRoleName \
        ParameterKey=EventBridgeRuleName,ParameterValue=$EventBridgeRuleName \
    --tags Key=project,Value=$PROJECT_NAME \
    --region $REGION \
    --disable-rollback
```

### Windows

``` powershell
$STACK_NAME="<cloudformation stack name>"
$PROJECT_NAME="<project name>"
$REGION="<region code>"

### CodeCommit Configuration
$CodeCommitStackName=""                     # [optional] The name of CodeCommit stack. (If you don't type anything, pipeline doesn't create source stage.)
$CodeCommitBranchName=""                    # [optional] The name of CodeCommit branch name for trigger pipeline.

### CodeBuild Configuration
$CodeBuildStackName=""                      # [optional] The name of CodeBuild stack. (If you don't type anything, pipeline doesn't create build stage.)

### CodeDeploy Configuration
$CodeDeployStackName=""                     # [optional] The name of CodeDeploy stack. (If you don't type anything, pipeline doesn't create deploy stage.)

### CodePipeline Configuration - Pipeline
$PipelineName=""                            # [REQUIRED] the name of CodePipeline pipeline.
$ServiceRoleName=""                         # [REQUIRED] The name of CodePipeline service IAM role.

### CodePipeline Configuration - Artifact Bucket
$ArtifactBucketName=""                      # [REQUIRED] The name of artifact S3 bucket.
$ArtifactEncryptionKeyId="alias/aws/s3"     # [optional] The key ARN, id, alias ARN, or name to encrypt artifact S3 bucket. (Default is alias/aws/s3)
$ArtifactLoggingDestinationBucketName=""    # [optional] The bucket name of artifact S3 bucket logging destination.
$ArtifactLoggingDestinationPrefix=""        # [optional] The log prefix of artifact S3 bucket logging.

### CodePipeline Configuration - Deploy
$TaskDefinitionTemplatePath="taskdef.json"  # [optional] The file name of the task definition.
$AppSpecTemplatePath="appspec.yaml"         # [optional] The file name of the appspec.

### CodePipeline Configuration - EventBridge
$EventBridgeRoleName=""                     # [optional] The name of EventBridge IAM role.
$EventBridgeRuleName=""                     # [optional] The name of EventBridge rule name.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/ecs/ci-cd/blue-green/codepipeline.yaml

# Using `deploy`
aws cloudformation deploy `
    --stack-name $STACK_NAME `
    --template-file ./codepipeline.yaml `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        CodeCommitStackName=$CodeCommitStackName `
        CodeCommitBranchName=$CodeCommitBranchName `
        CodeBuildStackName=$CodeBuildStackName `
        CodeDeployStackName=$CodeDeployStackName `
        PipelineName=$PipelineName `
        ServiceRoleName=$ServiceRoleName `
        ArtifactBucketName=$ArtifactBucketName `
        ArtifactEncryptionKeyId=$ArtifactEncryptionKeyId `
        ArtifactLoggingDestinationBucketName=$ArtifactLoggingDestinationBucketName `
        ArtifactLoggingDestinationPrefix=$ArtifactLoggingDestinationPrefix `
        TaskDefinitionTemplatePath=$TaskDefinitionTemplatePath `
        AppSpecTemplatePath=$AppSpecTemplatePath `
        EventBridgeRoleName=$EventBridgeRoleName `
        EventBridgeRuleName=$EventBridgeRuleName `
    --tags project=$PROJECT_NAME `
    --region $REGION `
    --disable-rollback

# Using `create-stack`
aws cloudformation create-stack `
    --stack-name $STACK_NAME `
    --template-body file://codepipeline.yaml `
    --parameters `
        ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME `
        ParameterKey=CodeCommitStackName,ParameterValue=$CodeCommitStackName `
        ParameterKey=CodeCommitBranchName,ParameterValue=$CodeCommitBranchName `
        ParameterKey=CodeBuildStackName,ParameterValue=$CodeBuildStackName `
        ParameterKey=CodeDeployStackName,ParameterValue=$CodeDeployStackName `
        ParameterKey=PipelineName,ParameterValue=$PipelineName `
        ParameterKey=ServiceRoleName,ParameterValue=$ServiceRoleName `
        ParameterKey=ArtifactBucketName,ParameterValue=$ArtifactBucketName `
        ParameterKey=ArtifactEncryptionKeyId,ParameterValue=$ArtifactEncryptionKeyId `
        ParameterKey=ArtifactLoggingDestinationBucketName,ParameterValue=$ArtifactLoggingDestinationBucketName `
        ParameterKey=ArtifactLoggingDestinationPrefix,ParameterValue=$ArtifactLoggingDestinationPrefix `
        ParameterKey=TaskDefinitionTemplatePath,ParameterValue=$TaskDefinitionTemplatePath `
        ParameterKey=AppSpecTemplatePath,ParameterValue=$AppSpecTemplatePath `
        ParameterKey=EventBridgeRoleName,ParameterValue=$EventBridgeRoleName `
        ParameterKey=EventBridgeRuleName,ParameterValue=$EventBridgeRuleName `
    --tags Key=project,Value=$PROJECT_NAME `
    --region $REGION `
    --disable-rollback
```