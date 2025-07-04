import aws_cdk
from aws_cdk import Stack, aws_lambda
from constructs import Construct
from ..configs import ROOT_DIR


class LamdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        aws_lambda.Function(
            self,
            "hello-function",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            handler="hello.lambda_handler",
            code=aws_lambda.Code.from_asset(
                str(ROOT_DIR / "assets"), exclude=["*", "!hello.py"]
            ),
        )
