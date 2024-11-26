import boto3
import zipfile
import os

def create_lambda_package():
    with zipfile.ZipFile('lambda_function.zip', 'w') as zipf:
        zipf.write('lambda_function.py')

def deploy_lambda_function():
    # Create the deployment package
    create_lambda_package()

    # Initialize a session using Amazon Lambda
    client = boto3.client('lambda')

    # Read the deployment package
    with open('lambda_function.zip', 'rb') as f:
        zipped_code = f.read()

    # Create or update the Lambda function
    response = client.create_function(
        FunctionName='my_lambda_function',
        Runtime='python3.8',
        Role='arn:aws:iam::account-id:role/execution_role',
        Handler='lambda_function.lambda_handler',
        Code=dict(ZipFile=zipped_code),
        Timeout=300, # Maximum allowable timeout
        MemorySize=128, # In MB
        Publish=True
    )

    print(response)

if __name__ == "__main__":
    deploy_lambda_function()
