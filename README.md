# YoutubeHashTagsGenerator

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- `main` - Code for the application's Lambda function.
- `events` - Invocation events that you can use to invoke the function.
- `tests` - Unit tests for the application code. 
- `template.yaml` - A template that defines the application's AWS resources.

## Application Overview

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

## IDE Integration

If you prefer to use an integrated development environment (IDE) to build and test your application, you can use the AWS Toolkit. The AWS Toolkit is an open-source plug-in for popular IDEs that uses the SAM CLI to build and deploy serverless applications on AWS. The AWS Toolkit also adds a simplified step-through debugging experience for Lambda function code. See the following links to get started:

* [CLion](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [GoLand](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [WebStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [Rider](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PhpStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [RubyMine](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [DataGrip](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

## Deploy the Sample Application

To deploy your application using SAM CLI, you need the following tools:

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Python 3 installed - [Python Downloads](https://www.python.org/downloads/)
* Docker - [Install Docker Community Edition](https://hub.docker.com/search/?type=edition&offering=community)

Run the following commands to build and deploy your application:

```bash
sam build --use-container
sam deploy --guided

Local Testing with SAM CLI
Build your application with the following command:

YoutubeHashTagsGenerator$ sam build --use-container
Test a single function by invoking it with a test event:

YoutubeHashTagsGenerator$ sam local invoke YoutubeHashTagsGeneratorFunction --event events/event.json
Emulate your application's API locally:

YoutubeHashTagsGenerator$ sam local start-api
YoutubeHashTagsGenerator$ curl http://localhost:3000/
Fetch, Tail, and Filter Lambda Function Logs
Fetch logs generated by your deployed Lambda function using the SAM CLI:

YoutubeHashTagsGenerator$ sam logs -n YoutubeHashTagsGeneratorFunction --stack-name "youtubehashtagsgenerator" --tail
## Tests

Install test dependencies and run tests:

YoutubeHashTagsGenerator$ pip install -r tests/requirements.txt --user
## unit test
YoutubeHashTagsGenerator$ python -m pytest tests/unit -v
# integration test
YoutubeHashTagsGenerator$ AWS_SAM_STACK_NAME="youtubehashtagsgenerator" python -m pytest tests/integration -v
## Cleanup
To delete the sample application, use the AWS CLI:

sam delete --stack-name "youtubehashtagsgenerator"
Additional Resources
AWS SAM Developer Guide
AWS Serverless Application Repository