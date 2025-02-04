pipeline {
    agent any // This specifies that the pipeline can run on any available agent

    stages {
        stage('Deploy') {
            steps {
                withAWS(credentials: 'AKIAYDWHS7D3CUT2ZNXR/******', region: 'us-east-1')
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
