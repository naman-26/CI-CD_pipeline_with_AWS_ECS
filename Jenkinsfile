#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        AWS_CREDS = credentials('naman-aws-creds')
        AWS_ACCOUNT_ID="YOUR_ACCOUNT_ID_HERE"
        AWS_DEFAULT_REGION="CREATED_AWS_ECR_CONTAINER_REPO_REGION" 
        IMAGE_REPO_NAME="ECR_REPO_NAME"
        IMAGE_TAG="IMAGE_TAG"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    }
    stages {
        stage("Login to AWS ECR") {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'aws-ecr-repo', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                        sh "echo $PASS | docker login -u $USER --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                    }
                }
            }
        }
        stage("build image") {
            steps {
                script {
                    echo "building the docker image..."
                    sh 'docker context use default'
                    sh 'docker compose -f docker-compose.yaml build'
                }
            }
        }
        stage('Pushing to ECR') {
            steps{  
                script {
                    echo "pushing the docker image to AWS ECR..."
                    sh "docker compose push ${REPOSITORY_URI}:${IMAGE_TAG}"
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying on AWS ECS...'
                sh 'docker context use myecscontext'
                sh 'docker compose -f docker-compose.yaml up'
                sh 'docker compose ps --format json'
            }
        }
    }   
}
