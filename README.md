# CI/CD pipeline with AWS ECS

A simple CI/CD pipeline which builds a docker container and runs it on AWS ECS which is configured for load-balancing.

Some important steps can be seen in this project, such as building Docker image, pushing a Docker image to ECR, and deploying Docker image on AWS ECS.

### Prerequisites
- Download and install the latest version of Docker Desktop
- Ensure you have an AWS account
- Create and Configure a Jenkins Server using Jenkins Docker image (https://hub.docker.com/_/jenkins)
- Create a AWS ECR repo, and rename the repo name in Jenkins file (https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html)
- Create AWS context, using docker context create ecs myecscontext command (https://docs.docker.com/cloud/ecs-integration/)


### Refrence
- https://flask.palletsprojects.com/en/2.0.x/quickstart/
- https://docs.docker.com/engine/reference/builder/
- https://www.jenkins.io/doc/book/pipeline/jenkinsfile/
- https://docs.docker.com/engine/reference/commandline/compose/
- https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html
