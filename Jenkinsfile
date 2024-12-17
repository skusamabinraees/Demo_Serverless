pipeline {
    agent any
    stages {
        stage('Change Dir') {
            steps {
                
                sh 'cd /usr/local/bin/'
            }
        }
        stage('Deploy') {
            steps {
                
                sh 'serverless deploy'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
    post {
        success {
            echo 'Deployment and tests successful!'
        }
        failure {
            echo 'Deployment or tests failed!'
        }
    }
}
