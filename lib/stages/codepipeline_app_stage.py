from aws_cdk import Stage
from constructs import Construct
from lib.stacks.web_server_stack import WebServerStack
from lib.stacks.api_lambda_s3_stack import ApiLambdaS3Stack

class PipelineAppStage(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        WebServerStack(scope=self, construct_id="WebServerStack")
        ApiLambdaS3Stack(scope=self, construct_id="ApiLambdaS3Stack")
