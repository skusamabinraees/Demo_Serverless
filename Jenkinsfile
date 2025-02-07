pipeline {
    agent any // This specifies that the pipeline can run on any available agent

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    env.PATH = "${env.PATH}:$/home/usama.s/.nvm/versions/node/v18.20.4/bin/serverless"
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'ls'
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
