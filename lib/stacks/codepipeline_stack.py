from aws_cdk import Stack
from aws_cdk.pipelines import (
    CodePipeline,
    CodePipelineSource,
    ShellStep,
    ManualApprovalStep,
)
from constructs import Construct
from lib.stages.codepipeline_app_stage import PipelineAppStage


class CodePipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # aws ci-cd code pipeline
        my_pipeline = CodePipeline(
            self,
            "MyPipeline",
            synth=ShellStep(
                id="Synth",
                input=CodePipelineSource.git_hub(
                    "ducchung2444/code-pipeline-cicd",
                    "master",
                ),
                commands=[
                    "curl -LsSf https://astral.sh/uv/install.sh | sh",
                    "export PATH=$HOME/.local/bin:$PATH",
                    "uv sync --no-dev",
                    "npm install -g aws-cdk",
                    "npx cdk synth",
                ],
            ),
        )
        test_stage = my_pipeline.add_stage(
            PipelineAppStage(self, "TestStage", env=kwargs.get("env"))
        )
        test_stage.add_post(ManualApprovalStep("ManualApproval"))

        my_pipeline.add_stage(
            PipelineAppStage(self, "ProdStage", env=kwargs.get("env"))
        )
