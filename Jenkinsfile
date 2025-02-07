pipeline {
     agent any
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
