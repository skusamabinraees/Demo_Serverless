pipeline {
     agent any
    environment {
    PATH = "${env./var/lib/jenkins/workspace/CICD_Test}/build-dir:${env./home/usama.s/Serverless/CICD}"
}

    stages {
        stage('Deploy') {
            steps {
                sh 'ls'
                sh 'pwd'
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
