pipeline {
     agent any
    stages {
        stage('Deploy') {
            steps {
                sh 'ls'
                sh 'pwd'
                export PATH=$PATH:/usr/local/share/dotnet:/usr/local/bin
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
