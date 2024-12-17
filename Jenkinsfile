pipeline {
    agent any
    stages {
        stage('Change Dir') {
            steps {
                
                'sh cd /home/vagrant/'
            }
        }
        stage('Deploy') {
            steps {
                
                'sh serverless deploy --config serverless.yml'
'
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
