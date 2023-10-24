# Nathan: Automated Alert Handling and Escalation Bot

Nathan is a real-time automated assistant that monitors alerts, reacts to them based on the runbook instructions, and escalates if necessary to the NOC team. All reactions, including response time, are documented for further analysis and system enhancement.

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Contribute](#contribute)
6. [License](#license)

## Features
- **Real-Time Monitoring**: Utilizes Slack WebSocket to monitor Slack channels in real-time.
- **OpenAI Integration**: Uses OpenAI API for alert exploitation and escalation.
- **Flexible Runbook Parsing**: Supports runbooks from GitLab/GoogleDocs and adapts to customer-specific runbooks.
- **Diverse Monitoring Systems**: Easily extendable to integrate with multiple monitoring systems.
- **AWS Integration**: Built for AWS Lambda and integrates with AWS DynamoDB for data storage.
- **Detailed Analytics**: Tracks alert counts, priorities, reactions, and NOC engineer response times.
- **Continuous Improvement**: Includes a feedback mechanism and supports automatic runbook updates.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.8 or higher.
- AWS CLI configured with appropriate permissions.
- Slack API token for integration.
- OpenAI API key for GPT-based decision making.

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/nathan.git
   cd nathan
Install Dependencies:
pip install -r requirements.txt
Configure Environment Variables:

## Modify config/lambda_env_variables.yaml with necessary details.
Ensure all API keys and tokens are securely stored.
Deployment:
Refer to docs/setup.md for a detailed deployment guide.

## Usage
After setup, Nathan will start monitoring the configured Slack channels in real-time. It will:

## Process and prioritize alerts.
Act based on the instructions in the runbook.
Escalate to NOC if necessary.
Document all actions for analytics.
For detailed usage instructions, refer to docs/usage.md.

## Contribute
If you want to contribute to Nathan, check out the CONTRIBUTING.md file on how to get started. We welcome pull requests, issues, and feedback.