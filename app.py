#!/usr/bin/env python3
import os

import aws_cdk as cdk

# from lib.stacks.api_lambda_s3_stack import ApiLambdaS3Stack
from lib.stacks.web_server_stack import WebServerStack


app = cdk.App()

WebServerStack(
    app,
    "WebServerStack",
    env=cdk.Environment(account="423307327132", region="ap-east-1"),
)

app.synth()
