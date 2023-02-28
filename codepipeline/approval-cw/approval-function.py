import boto3
from botocore.config import Config

class CannotFoundParameterException(Exception):
    parameter_name: str = ''

    def __init__(self, parameter_name) -> None:
        self.parameter_name = parameter_name
    
    def __str__(self) -> str:
        return f'Cannot found parameter "{self.parameter_name}"'

def put_approval_result(pipeline_name, stage_name, action_name, summary, status, token, region):
    client = boto3.client('codepipeline', config=Config(region_name=region))
    response = client.put_approval_result(
        pipelineName=pipeline_name,
        stageName=stage_name,
        actionName=action_name,
        result={
            'summary': summary,
            'status': status
        },
        token=token
    )

    return str(response['approvedAt'])

def lambda_handler(event, context):
    status = event.get('status', None)
    pipeline_name = event.get('pipeline_name', None)
    stage_name = event.get('stage_name', None)
    action_name = event.get('action_name', None)
    token = event.get('token', None)
    summary = event['widgetContext']['forms']['all'].get('summary')
    region = event.get('region', None)

    try:
        if status is None:
            raise CannotFoundParameterException('status')
        
        elif pipeline_name is None:
            raise CannotFoundParameterException('pipeline_name')

        elif stage_name is None:
            raise CannotFoundParameterException('stage_name')
        
        elif action_name is None:
            raise CannotFoundParameterException('action_name')
        
        elif token is None:
            raise CannotFoundParameterException('token')
        
        elif summary is None:
            raise CannotFoundParameterException('summary')

        elif region is None:
            raise CannotFoundParameterException('region')
        
        else:
            approved_at = put_approval_result(pipeline_name, stage_name, action_name, summary, status, token, region)

            return f'Approved at {approved_at}'
    
    except CannotFoundParameterException as e:
        return e.__str__()