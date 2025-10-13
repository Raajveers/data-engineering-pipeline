pipeline {
    agent any

    environment {
        IMAGE_NAME = 'data-engineering-pipeline'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Container') {
            steps {
                echo 'Running Docker container...'
                sh 'docker run --rm $IMAGE_NAME'
            }
        }
    }

    post {
        always {
            echo "✅ Pipeline completed."
        }
    }
}

