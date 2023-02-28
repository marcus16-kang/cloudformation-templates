import os
import boto3
from botocore.config import Config

DOCS = '''
## Approve or Reject Pipeline

Put approve or reject CI/CD pipeline using CodePipeline.

### Widget Parameters

| Param                             | Descriotion                  |
|-----------------------------------|------------------------------|
| **pipeline-arn**                  | The arn of the pipeline.     |
| **pipeline-approval-stage-name**  | The name of approval stage.  |
| **pipeline-approval-action-name** | The name of approval action. |

### Example parameters

``` json
{
    "pipeline-arn": "arn:aws:codepipeline:us-east-1:123456789012:test-pipeline",
    "pipeline-approval-stage-name": "Approval",
    "pipeline-approval-action-name": "Approval"
}
```
'''

class PipelineNotFoundException(Exception):
    pipeline_name: str = ''
    region: str = ''

    def __init__(self, pipeline_name, region) -> None:
        self.pipeline_name = pipeline_name
        self.region = region

    def __str__(self) -> str:
        return f'Cannot found pipeline "{self.pipeline_name}" in "{self.region}".'

class StateNotFoundException(Exception):
    stage_name: str = ''

    def __init__(self, stage_name) -> None:
        self.stage_name = stage_name

    def __str__(self) -> str:
        return f'Cannot found approval state "{self.stage_name}".'

class ActionNotFoundException(Exception):
    action_name: str = ''

    def __init__(self, action_name) -> None:
        self.action_name = action_name

    def __str__(self) -> str:
        return f'Cannot found approval action "{self.action_name}".'


def get_approval_state(region, pipeline_name, approval_stage_name):
    try:
        client = boto3.client('codepipeline', config=Config(region_name=region))
        response = client.get_pipeline_state(
            name=pipeline_name
        )
        find_approval_state = [item for item in response['stageStates'] if item['stageName'] == approval_stage_name]

        if len(find_approval_state) <= 0:
            raise StateNotFoundException(approval_stage_name)
        
        else:
            return find_approval_state[0]

    except client.exceptions.PipelineNotFoundException:
        raise PipelineNotFoundException(pipeline_name, region)

def get_approval_action(state, action_name):
    find_approval_action = [item for item in state['actionStates'] if item['actionName'] == action_name]

    if len(find_approval_action) <= 0:
        raise ActionNotFoundException(action_name)
    
    else:
        return find_approval_action[0]        

def get_approval_status_and_token(action):
    if action.get('latestExecution', None):
        if action['latestExecution']['status'] == 'InProgress':
            return True, action['latestExecution']['token']
        
        else:
            return False, None
    
    else:
        return False, None

def create_html(pipeline_name, need_approval, put_approval_result_function_arn, stage_name, action_name, token, region):
    html = f'''
        <h3>{pipeline_name}</h3>
    '''

    if need_approval:
        html += f'''
            <p>
                <span>Summary</span>
                <input type="text" name="summary">
            </p>
            <a class="btn btn-primary">Approve</a>
            <cwdb-action action="call" endpoint="{put_approval_result_function_arn}" display="popup" confirmation="Are you sure you want to approve?">
                {{ "status": "Approved", "pipeline_name": "{pipeline_name}", "stage_name": "{stage_name}", "action_name": "{action_name}", "token": "{token}", "region": "{region}" }}
            </cwdb-action>
            <a class="btn btn-danger">Reject</a>
            <cwdb-action action="call" endpoint="{put_approval_result_function_arn}" display="popup" confirmation="Are you sure you want to reject?">
                {{ "status": "Rejected", "pipeline_name": "{pipeline_name}", "stage_name": "{stage_name}", "action_name": "{action_name}", "token": "{token}", "region": "{region}" }}
            </cwdb-action>
        '''
    
    else:
        html += f'''
            <p>
                <span>Summary</span>
                <input type="text" name="summary" disabled>
            </p>
            <a class="btn disabled">Approve</a>
            <a class="btn disabled">Reject</a>
        '''

    return html


def lambda_handler(event, context):
    if event.get('describe', None):
        return DOCS

    if os.getenv('PUT_APPROVAL_RESULT_FUNCTION_ARN', None) is None:
        return 'Please enter the put approval result function arn in functoin\'s environment variable. ("PUT_APPROVAL_RESULT_FUNCTION_ARN")'
    
    if event.get('pipeline-arn', None) is None:
        return 'Please enter the pipeline arn in parameter. ("pipeline-arn")'
    
    elif event.get('pipeline-approval-stage-name', None) is None:
        return 'Please enter the approval stage name in parameter. ("pipeline-approval-stage-name")'
    
    elif event.get('pipeline-approval-action-name', None) is None:
        return 'Please enter the approval action name in parameter. ("pipeline-approval-action-name")'
    
    else:
        put_approval_result_function_arn = os.getenv('PUT_APPROVAL_RESULT_FUNCTION_ARN')
        pipeline_arn = event['pipeline-arn']
        arn_split = pipeline_arn.split(':')
        region = arn_split[3]
        pipeline_name = arn_split[5]
        approval_stage_name = event['pipeline-approval-stage-name']
        approval_action_name = event['pipeline-approval-action-name']

        try:
            approval_state = get_approval_state(region, pipeline_name, approval_stage_name)
            approval_action = get_approval_action(approval_state, approval_action_name)
            approval_status, approval_token = get_approval_status_and_token(approval_action)

            html = create_html(pipeline_name, approval_status, put_approval_result_function_arn, approval_stage_name, approval_action_name, approval_token, region)

            return html

        except PipelineNotFoundException as e:
            return e.__str__()

        except StateNotFoundException as e:
            return e.__str__()
        
        except ActionNotFoundException as e:
            return e.__str__()