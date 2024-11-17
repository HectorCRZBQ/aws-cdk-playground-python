from aws_cdk import (
    Stack,
    CfnOutput,
    aws_iam as iam
)
from constructs import Construct

class CdkIamLabStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Crear grupo de Power Users
        power_users_group = iam.Group(
            self, 'PowerUsersGroup',
            group_name='power-users'
        )

        # Adjuntar política PowerUserAccess al grupo
        power_users_group.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name('PowerUserAccess')
        )

        # Crear usuario IAM
        user = iam.User(
            self, 'PowerUser',
            user_name='power-user-cdk',
            groups=[power_users_group]
        )

        # Crear access key para el usuario
        access_key = iam.CfnAccessKey(
            self, 'PowerUserAccessKey',
            user_name=user.user_name
        )
        
        # Outputs para obtener las credenciales
        CfnOutput(
            self, 'AccessKeyId',
            value=access_key.ref
        )