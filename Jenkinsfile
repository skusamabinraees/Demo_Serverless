pipeline {
    agent any // This specifies that the pipeline can run on any available agent

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
                sh 'sls deploy' // Deploy the application
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
