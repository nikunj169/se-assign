pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "YOUR_DOCKERHUB_USERNAME/imt2023068"
        DOCKER_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Pull Code from GitHub') {
            steps {
                echo 'Pulling code from GitHub...'
                checkout scm
            }
        }
        
        stage('Build Code') {
            steps {
                echo 'Building the application...'
                sh 'python3 --version'
                sh 'ls -la'
            }
        }
        
        stage('Test Code') {
            steps {
                echo 'Running tests...'
                sh 'python3 -m unittest test_calculator.py -v'
            }
        }
        
        stage('Create Docker Image') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo 'Building Docker image...'
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                    sh "docker build -t ${DOCKER_IMAGE}:latest ."
                }
            }
        }
        
        stage('Verify Docker Image') {
            steps {
                echo 'Verifying Docker image creation...'
                sh 'docker images | grep imt2023068'
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', 
                                                     usernameVariable: 'DOCKER_USER', 
                                                     passwordVariable: 'DOCKER_PASS')]) {
                        sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                        sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                        sh "docker push ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
            echo "Docker image pushed: ${DOCKER_IMAGE}:${DOCKER_TAG}"
        }
        failure {
            echo 'Pipeline failed! Check logs for details.'
        }
        always {
            sh 'docker logout'
        }
    }
}
