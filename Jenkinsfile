pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                sh 'cd /home/vagrant/'
                sh 'serverless deploy --config /home/vagrant/serverless.yml'
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
