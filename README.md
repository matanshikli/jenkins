#  Jenkins pipe

## Overview
This project automates the deployment of a Python application that interacts with AWS EC2 to monitor Kubernetes clusters. It runs every 5 minutes, checks for running EC2 instances with specific tags, and logs the information as JSON.

## Dockerfile
The Dockerfile is a multi-stage build:
1. **Building Dependencies**: Installs Python packages.
2. **Linter Setup (Flake8)**: Checks code quality but does not fail the build.
3. **Final Image**: Uses Python Alpine for a lightweight container.

## Application
The Python application uses `boto3` to query AWS EC2 instances and the `python-json-logger` for logging.

## Jenkins Pipeline
- The pipeline triggers on every push to the `development` branch.
- It builds a Docker image tagged with the Jenkins build number.
- If the build is successful, it automatically merges the code to the `master` branch.

### Setting Up Jenkins
1. The Jenkins server should have Docker installed and configured (`Dockerfile.jenkins` file)
2. Install GitHub and DSL plugins
3. Add GitHub auth token with push rights to Jenkins credentials 
4. Create a new freestyle job and connect your GitHub repo with source management
5. Use the provided Job DSL script to create the Jenkins job.
6. The job listens for changes in the `development` branch and executes the pipeline.

### Setting Up GitHub

1. create a webhook from your repo to your Jenkins server, for ex: http://54.78.159.13:8080/github-webhook
2. create personal access token

### Running the Pipeline
1. Push code to the `development` branch.
2. Jenkins automatically triggers the build (you need to approve the DSL script first).
3. Check build logs for success or failure.
4. On successful build, code is merged to `main`.

### Testing the Application
- Run the Docker container locally to test the application.
- Ensure AWS credentials are correctly configured.

## Note
- Ensure that AWS credentials are securely managed.
- Modify the scheduling time as needed through environment variables.
