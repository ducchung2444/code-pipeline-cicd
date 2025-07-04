from aws_cdk import Stack
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from constructs import Construct


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
                commands=["npm ci", "npm run build", "npx cdk synth"],
            ),
        )
