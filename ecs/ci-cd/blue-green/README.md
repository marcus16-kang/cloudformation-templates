# ECS Blue-Green CI/CD

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

### Deploy

``` shell
STACK_NAME="<cloudformation stack name>"
PROJECT_NAME="<project name>"
REPOSITORY_NAME="<codecommit repository name>"
ENABLE_NOTIFICATION="enable"    # enable or disable
# NOTIFICATION_TOPIC_NAME="<sns topic name>"
# NOTIFICATION_TOPIC_ENCRYPTION_KEY="<kms key id, arn, alias name, arn>"
REGION="<region code>"

wget <LINK>

aws cloudformation deploy \
    --template-file ./codecommit.yaml \
    --stack-name $STACK_NAME \
    --parameter-overrides \
        ProjectName=$PROJECT_NAME \
        RepositoryName=$REPOSITORY_NAME \
        EnableNotification=$ENABLE_NOTIFICATION \
        # NotificationTopicName=$NOTIFICATION_TOPIC_NAME \
        # NotificationTopicEncryptionKey=$NOTIFICATION_TOPIC_ENCRYPTION_KEY \
    --tags project=$PROJECT_NAME \
    --region $REGION
```