pipeline {
     agent any
    stages {
        stage('Install Serverless') {
            steps {
                sh 'sudo npm install serverless@3'
            }
        }

        stage('Deploy Serverless Application') {
            steps {
                sh 'serverless deploy'
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
