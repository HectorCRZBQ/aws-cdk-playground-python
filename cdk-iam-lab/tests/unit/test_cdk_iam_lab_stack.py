import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_iam_lab.cdk_iam_lab_stack import CdkIamLabStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_iam_lab/cdk_iam_lab_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkIamLabStack(app, "cdk-iam-lab")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
