pipeline {
    agent any // This specifies that the pipeline can run on any available agent

    stages {
        stage('Deploy') {
            steps {
                sh 'cd CICD/CICD-New/CICD',
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
