pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                sh 'sls deploy'
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
