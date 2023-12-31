#  Jenkins project

## Overview
This project automates the deployment of a Python application that interacts with AWS EC2 to monitor Kubernetes clusters.

### Python application
The app uses `boto3` to query AWS EC2 instances and the `python-json-logger` for logging.

### Dockerfile
The Dockerfile is a multi-stage build:
1. **Building Dependencies**: Installs Python packages.
2. **Linter Setup (Flake8)**: Checks code quality but does not fail the build.
3. **Final Image**: Uses Python Alpine for a lightweight container.

### Jenkins Pipeline
- The pipeline triggers on every push to the `development` branch.
- It builds a Docker image tagged with the Jenkins build number, and with the AWS credentials.
- If the build is successful, it automatically merges the code to the `master` branch.

## Setup

### Setting Up AWS
1. create access key with the right permissions

### Setting Up GitHub
1. create a webhook from your repo to your Jenkins server, for ex: http://54.78.159.13:8080/github-webhook
2. create personal access token

### Setting Up Jenkins
1. The Jenkins server should have Docker installed and configured (`Dockerfile.jenkins` file)
2. Install GitHub and DSL plugins
3. Credentials in Jenkins:
  - Add GitHub auth token with push rights to Jenkins credentials (username and password) with the ID 'GITHUB_AUTH'
  - Add AWS credentials to Jenkins credentials under the ID 'AWS_AUTH', save the key ID in the user name field.
  - Add AWS default region to Jenkins credentials under the ID 'AWS_DEFAULT', save the value under the password with empty user name.
4. Create a new freestyle job and connect your GitHub repo with source management
4. Use the provided Job DSL script to create the Jenkins job.
5. The job listens for changes in the `development` branch and executes the pipeline.

## Running the Pipeline
1. Push code to the `development` branch.
2. Jenkins automatically triggers the build (you need to approve the DSL script first).
3. Check build logs for success or failure.
4. On successful build, code is merged to `main`.

![image](https://github.com/matanshikli/jenkins/assets/106749791/fe70cfa5-80ae-44ae-a5d4-db3c3d1e25e1)
