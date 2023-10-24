#!/bin/bash

# Define AWS CLI profile name (change if necessary)
PROFILE="default"

# Define AWS region (change if necessary)
REGION="us-west-1"

# Name of the Lambda deployment package
PACKAGE_NAME="nathan_lambda_package.zip"

# Name of the Lambda function
LAMBDA_FUNCTION_NAME="NathanLambdaFunction"

# S3 bucket for Lambda deployment package
S3_BUCKET="nathan-lambda-deployment-bucket"

# Create a deployment package
echo "Creating deployment package..."
zip -r $PACKAGE_NAME . -x "*.git*" "deploy_script.sh"

# Upload deployment package to S3
echo "Uploading deployment package to S3..."
aws s3 cp $PACKAGE_NAME s3://$S3_BUCKET/ --profile $PROFILE

# Create or update Lambda function
echo "Deploying Lambda function..."
aws lambda update-function-code --function-name $LAMBDA_FUNCTION_NAME --s3-bucket $S3_BUCKET --s3-key $PACKAGE_NAME --publish --profile $PROFILE --region $REGION

# Clean up
rm $PACKAGE_NAME

echo "Deployment completed."

