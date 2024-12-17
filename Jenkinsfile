pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                sh '/home/vagrant/Demo_Serverless'
                sh 'ls'
                sh 'serverless deploy --config serverless.yml'
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
