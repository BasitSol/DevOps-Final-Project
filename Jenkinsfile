pipeline {
    agent any // Specifies that the pipeline can run on any available agent

    environment {
        // Defined environment variables to be used in the pipeline
        DOCKER_IMAGE = 'basitdock09/final-devops-dhub'
        // This is the ID of the 'Username with password' credential created in Jenkins
        DOCKER_CREDENTIALS_ID = 'docker-hub-creds'
    }

    stages {
            {
            }
        stage('Build Docker Image') {
            steps {
                //This is gonna be the last one to build for
                // Execute a shell command to build the Docker image
                // The Dockerfile is located in the 'backend' directory relative to the repository root
                sh 'docker build -t $DOCKER_IMAGE ./backend'
            }
        }

        stage('Push to DockerHub') {
            steps {
                // Use 'withCredentials' to securely access the Docker Hub credentials
                withCredentials([usernamePassword(credentialsId: "$DOCKER_CREDENTIALS_ID", passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    // Log in to Docker Hub using the injected username and password
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    // Push the built Docker image to Docker Hub
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }
    }
}

