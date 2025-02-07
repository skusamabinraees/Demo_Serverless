pipeline {
     agent any
    stages {
        stage('Deploy') {
            steps {
                sh 'ls'
                sh 'pwd'
                #sh 'export PATH=$PATH:/home/usama.s/.nvm/versions/node/v23.7.0/bin/sls:/usr/local/bin'
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
