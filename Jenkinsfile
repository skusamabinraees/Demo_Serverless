pipeline {
     agent any
         environment {
        PATH = "${env./var/lib/jenkins}/build-dir:${env.HOME}/Serverless/CICD:${env.PATH}"
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
