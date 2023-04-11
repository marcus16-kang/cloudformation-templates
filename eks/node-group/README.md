# EKS NodeGroup with Launch Template

## Note

If you want to add labels or taints, you should update template file manually.

``` yaml
  NodeGroup:
    Type: AWS::EKS::Nodegroup
    Properties:
      ...
      # Labels:
      #   key1: value1
      #   key2: value2
      # Taints:
      #   - Effect: 
      #     Key: 
      #     Value: 
```

## Linux

``` bash
STACK_NAME=""
PROJECT_NAME=""
REGION_CODE=""

### Launch Template Configuration
LaunchTemplateName=""   # [REQUIRED] he name of this launch template.
InstanceName=""         # [REQUIRED] The name of EC2 instance.
SecurityGroupIds=""     # [REQUIRED] The ids of security group for EC2 instances.

### NodeGroup Configuration
ClusterName=""          # [REQUIRED] The name of eks cluster.
NodeGroupName=""        # [REQUIRED] The name of eks nodegroup.
AmiType=""              # [REQUIRED] The ami type of nodegroup's EC2 instances.
# AL2_x86_64 | AL2_x86_64_GPU | AL2_ARM_64
# BOTTLEROCKET_x86_64 | BOTTLEROCKET_ARM_64 | BOTTLEROCKET_x86_64_NVIDIA | BOTTLEROCKET_ARM_64_NVIDIA
# WINDOWS_CORE_2019_x86_64 | WINDOWS_CORE_2022_x86_64 | WINDOWS_FULL_2019_x86_64 | WINDOWS_FULL_2022_x86_64 | CUSTOM
CapacityType=""         # `ON_DEMAND` or `SPOT` | [REQUIRED] The capacity type of nodegroup's EC2 instances.
InstanceTypes=""        # [REQUIRED] The instance types of nodegroup's EC2 instances.
NodeRoleArn=""          # [REQUIRED] The role arn of nodegroup's EC2 instances.
DesiredSize=""          # [REQUIRED] The number of desired size.
MinSize=""              # [REQUIRED] The number of min size.
MaxSize=""              # [REQUIRED] The number of max size.
Subnets=""              # [REQUIRED] The subnet ids of nodegroup's EC2 instances.

curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/node-group/eks-nodegroup.yaml

### If you want to add labels to nodegroup, using this command.
# echo "
#       Labels:
#         key1: value1
#         key2: value2
# " >> eks-nodegroup.yaml

### If you want to add taints to nodegroup, using this command.
# echo "
#       Taints:
#         - Effect: # `NO_SCHEDULE` | `NO_EXECUTE` | `PREFER_NO_SCHEDULE`
#           Key:
#           Value:
# " >> eks-nodegroup.yaml


aws cloudformation deploy \
    --template-file ./eks-nodegroup.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        LaunchTemplateName=$LaunchTemplateName \
        InstanceName=$InstanceName \
        SecurityGroupIds=$SecurityGroupIds \
        ClusterName=$ClusterName \
        NodeGroupName=$NodeGroupName \
        AmiType=$AmiType \
        CapacityType=$CapacityType \
        InstanceTypes=$InstanceTypes \
        NodeRoleArn=$NodeRoleArn \
        DesiredSize=$DesiredSize \
        MinSize=$MinSize \
        MaxSize=$MaxSize \
        Subnets=$Subnets \
    --disable-rollback \
    --tags project=$PROJECT_NAME \
    --region $REGION
```

## Windows

``` powershell
$STACK_NAME=""
$PROJECT_NAME=""
$REGION_CODE=""

### Launch Template Configuration
$LaunchTemplateName=""   # [REQUIRED] he name of this launch template.
$InstanceName=""         # [REQUIRED] The name of EC2 instance.
$SecurityGroupIds=""     # [REQUIRED] The ids of security group for EC2 instances.

### NodeGroup Configuration
$ClusterName=""          # [REQUIRED] The name of eks cluster.
$NodeGroupName=""        # [REQUIRED] The name of eks nodegroup.
$AmiType=""              # [REQUIRED] The ami type of nodegroup's EC2 instances.
# AL2_x86_64 | AL2_x86_64_GPU | AL2_ARM_64
# BOTTLEROCKET_x86_64 | BOTTLEROCKET_ARM_64 | BOTTLEROCKET_x86_64_NVIDIA | BOTTLEROCKET_ARM_64_NVIDIA
# WINDOWS_CORE_2019_x86_64 | WINDOWS_CORE_2022_x86_64 | WINDOWS_FULL_2019_x86_64 | WINDOWS_FULL_2022_x86_64 | CUSTOM
$CapacityType=""         # `ON_DEMAND` or `SPOT` | [REQUIRED] The capacity type of nodegroup's EC2 instances.
$InstanceTypes=""        # [REQUIRED] The instance types of nodegroup's EC2 instances.
$NodeRoleArn=""          # [REQUIRED] The role arn of nodegroup's EC2 instances.
$DesiredSize=""          # [REQUIRED] The number of desired size.
$MinSize=""              # [REQUIRED] The number of min size.
$MaxSize=""              # [REQUIRED] The number of max size.
$Subnets=""              # [REQUIRED] The subnet ids of nodegroup's EC2 instances.

curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/node-group/eks-nodegroup.yaml

### If you want to add labels to nodegroup, using this command.
# Add-Content -Path eks-nodegroup.yaml -Value @"
#       Labels:
#         key1: value1
#         key2: value2
# "@

### If you want to add taints to nodegroup, using this command.
# Add-Content -Path eks-nodegroup.yaml -Value @"
#       Taints:
#         - Effect: # `NO_SCHEDULE` | `NO_EXECUTE` | `PREFER_NO_SCHEDULE`
#           Key:
#           Value:
# "@

aws cloudformation deploy `
    --template-file ./eks-nodegroup.yaml `
    --stack-name $STACK_NAME `
    --parameter-overrides `
        ProjectName=$PROJECT_NAME `
        LaunchTemplateName=$LaunchTemplateName `
        InstanceName=$InstanceName `
        SecurityGroupIds=$SecurityGroupIds `
        ClusterName=$ClusterName `
        NodeGroupName=$NodeGroupName `
        AmiType=$AmiType `
        CapacityType=$CapacityType `
        InstanceTypes=$InstanceTypes `
        NodeRoleArn=$NodeRoleArn `
        DesiredSize=$DesiredSize `
        MinSize=$MinSize `
        MaxSize=$MaxSize `
        Subnets=$Subnets `
    --disable-rollback `
    --tags project=$PROJECT_NAME `
    --region $REGION
```