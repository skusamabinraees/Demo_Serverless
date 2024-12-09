pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                sh 'sls create --template aws-python3 --path myService'
                sh 'cd myService'
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
