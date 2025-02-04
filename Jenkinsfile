pipeline {
      agent {
        docker {
            image 'python:3.9' // Use a Python 3.9 Docker image
            args '-u root' // Run as root to install dependencies
        }
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/skusamabinraees/Demo_Serverless.git'
            }
        }
        stage('Build') {
            steps {
                sh 'sls package' // Package the serverless application
            }
        }

        stage('Deploy') {
            steps {
                sh 'sls deploy' // Deploy the application locally or to a specified environment
            }
        }
    }

    post {
        success {
            echo 'Deployment was successful!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
