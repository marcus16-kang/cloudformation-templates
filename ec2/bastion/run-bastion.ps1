$STACK_NAME = "<cloudformation stack name>"
$REGION = "<region code>"

$INSTANCE_NAME = "<instance name>"
$INSTANCE_TYPE = "<instance type>"
$INSTANCE_VPC = "<instance vpc id>"
$INSTANCE_SUBNET = "<instance subnet>"
$INSTANCE_SSH_PORT = "<instance ssh port>"
$INSTANCE_SSH_PASSWORD = "<instance ssh password>"
$INSTANCE_EIP_NAME = "<instance eip name>"
$INSTANCE_SECURITY_GROUP_NAME = "<instance security group name>"
$INSTANCE_ROLE_NAME = "<instance role name>"

# https://gist.github.com/altrive/72594b8427b2fff16431
function Notification {
    $ErrorActionPreference = "Stop"

    $notificationTitle = "Bastion Server Created."

    [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null
    $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText01)

    #Convert to .NET type for XML manipuration
    $toastXml = [xml] $template.GetXml()
    $toastXml.GetElementsByTagName("text").AppendChild($toastXml.CreateTextNode($notificationTitle)) > $null

    #Convert back to WinRT type
    $xml = New-Object Windows.Data.Xml.Dom.XmlDocument
    $xml.LoadXml($toastXml.OuterXml)

    $toast = [Windows.UI.Notifications.ToastNotification]::new($xml)
    $toast.Tag = "PowerShell"
    $toast.Group = "PowerShell"
    $toast.ExpirationTime = [DateTimeOffset]::Now.AddMinutes(5)
    #$toast.SuppressPopup = $true

    $notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("PowerShell")
    $notifier.Show($toast);
}

Invoke-WebRequest -Uri https://github.com/marcus16-kang/cloudformation-templates/blob/main/ec2/bastion.yaml?raw=true -OutFile ./bastion.yaml

aws cloudformation create-stack `
    --stack-name $STACK_NAME `
    --template-body file://bastion.yaml `
    --parameters `
        ParameterKey=InstanceName,ParameterValue=$INSTANCE_NAME `
        ParameterKey=InstanceType,ParameterValue=$INSTANCE_TYPE `
        ParameterKey=InstanceVPC,ParameterValue=$INSTANCE_VPC `
        ParameterKey=InstanceSubnet,ParameterValue=$INSTANCE_SUBNET `
        ParameterKey=InstanceSSHPort,ParameterValue=$INSTANCE_SSH_PORT `
        ParameterKey=InstanceSSHPassword,ParameterValue=$INSTANCE_SSH_PASSWORD `
        ParameterKey=InstanceEIPName,ParameterValue=$INSTANCE_EIP_NAME `
        ParameterKey=InstanceSecurityGroupName,ParameterValue=$INSTANCE_SECURITY_GROUP_NAME `
        ParameterKey=InstanceRoleName,ParameterValue=$INSTANCE_ROLE_NAME `
    --capabilities CAPABILITY_IAM `
    --region $REGION

aws cloudformation wait stack-create-complete `
    --stack-name $STACK_NAME `
    --region $REGION

Notification

aws cloudformation describe-stacks `
    --stack-name $STACK_NAME `
    --query 'Stacks[0].Outputs[?OutputKey==`PuttyCommand`].OutputValue' `
    --output text | powershell -
