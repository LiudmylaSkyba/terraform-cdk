from imports.aws import AwsProvider
from imports.aws.s3 import S3Bucket, S3BucketWebsite

# DOCS_BLOCK_START:constructs-scope

from constructs import Construct
from cdktf import App, TerraformStack

class PublicS3Bucket(Construct):

    bucket: S3Bucket
    
    def __init__(self, scope: Construct, name: str):
        super().__init__(scope, name) # This creates a new scope since we extend from construct

        AwsProvider(self, "aws",
            region = "us-east-1"
        )

        # This bucket is in a different scope than the buckets
        # defined in `MyStack`. Therefore, it does not need a unique name.
        self.bucket = S3Bucket(self, "bucket",
            bucket_prefix = name,
            website = S3BucketWebsite(
                index_document = "index.html",
                error_document = "5xx.html",
            )
        )


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, name: str):
        super().__init__(scope, name)

        # Both buckets are inside of the same stack, meaning they share
        # the same scope. Therefore, their names must be unique.
        PublicS3Bucket(self, "first-bucket")
        PublicS3Bucket(self, "second-bucket")
# DOCS_BLOCK_END:constructs-scope

# DOCS_BLOCK_START:constructs-use-constructs
import os
import imports.kubernetes as kubernetes
from my_constructs import KubernetesWebAppDeployment

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, name: str):
        super().__init__(scope, name)
        kubernetes.KubernetesProvider(self, "kind",
                                      config_path=os.path.join(os.path.dirname(
                                          __file__), '..', 'kubeconfig.yaml')
                                      )

        KubernetesWebAppDeployment(self, "deployment",
                                   image="nginx:latest",
                                   replicas=2,
                                   app="myapp",
                                   component="frontend",
                                   environment="dev"
                                   )


app = App()
MyStack(app, "demo")
app.synth()
# DOCS_BLOCK_END:constructs-use-constructs
