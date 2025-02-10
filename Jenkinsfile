pipeline {
     agent any
    stages {
        stage('Install Serverless') {
            steps {
                sh 'npm install serverless@3'
                sh 'npx serverless deploy' 
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
