pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }
        stage('Deploy Serverless') {
            steps {
                sh 'serverless deploy'
            }
        }
    }
}
