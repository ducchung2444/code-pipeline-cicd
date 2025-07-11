import aws_cdk
from aws_cdk import (
    Stack,
    aws_s3 as s3
)
from constructs import Construct

class S3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        s3_bucket = s3.Bucket(self, id="buket-6969",
            bucket_name='chungyeuduong69',
            versioned=True,
            removal_policy=aws_cdk.RemovalPolicy.DESTROY,  # Destroys bucket on `cdk destroy`
            auto_delete_objects=True                    # Deletes all objects automatically
        )
