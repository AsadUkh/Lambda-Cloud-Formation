from aws_cdk import (
    aws_events as events,
    aws_lambda as lambda_,
    aws_events_targets as targets,
    aws_iam as iam,
    core,
)


class LambdaCronStack(core.Stack):
    def __init__(self, app: core.App, id: str) -> None:
        super().__init__(app, id)

        with open("lambda-handler.py", encoding="utf8") as fp:
            handler_code = fp.read()

        lambdaFn = lambda_.Function(
            self, "renew-api-key-expiration",
            code=lambda_.InlineCode(handler_code),
            handler="index.main",
            timeout=core.Duration.seconds(900),
            runtime=lambda_.Runtime.PYTHON_3_7,
        )

        lambdaFn.add_to_role_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=['appsync:ListApiKeys','appsync:UpdateApiKey'],
                resources=['*'],
                ))
        
        rule = events.Rule(
            self, "Rule",
            schedule=events.Schedule.rate(core.Duration.days(1)),
        )
        rule.add_target(targets.LambdaFunction(lambdaFn))


app = core.App()
LambdaCronStack(app, "Lambda-Test-AppSync")
app.synth()
