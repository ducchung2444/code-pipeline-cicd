import aws_cdk
from aws_cdk import (
    Stack,
    aws_lambda,
    aws_s3 as s3,
    aws_iam as iam,
    aws_apigateway as apigateway,
)
from constructs import Construct
from ..configs import ASSET_DIR


class ApiLambdaS3Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # bucket
        balance_status_s3 = s3.Bucket(
            self,
            "balance_status_s3",
            bucket_name="balerina-capuchina-mimi",
            versioned=True,
            removal_policy=aws_cdk.RemovalPolicy.DESTROY,  # Destroys bucket on `cdk destroy`
            auto_delete_objects=True,  # Deletes all objects automatically
        )
        # ---
        # iam
        iam_balance_status_role = iam.Role(
            self,
            "iam_balenciaga",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            description="role for lambda to access s3 bucket",
            role_name="banking_lambda_role",
        )
        # add policy for s3
        iam_balance_status_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
        )
        # ---
        # lambda
        banking_lambda = aws_lambda.Function(
            self,
            "bank-lambda",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            handler="banking.lambda_handler",
            code=aws_lambda.Code.from_asset(
                str(ASSET_DIR), exclude=["*", "!banking.py"]
            ),
            role=iam_balance_status_role,
        )

        banking_rest_api = apigateway.LambdaRestApi(
            self,
            "banking_rest_apigw",
            handler=banking_lambda,
            rest_api_name="banking_rest_api",
            deploy=True,
            proxy=False,
        )
        bank_status = banking_rest_api.root.add_resource("bank_status")
        bank_status.add_method("GET")
