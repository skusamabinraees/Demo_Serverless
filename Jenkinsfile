pipeline {
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
