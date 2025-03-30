pipeline {
    agent {
        docker { image 'python:3.12'}
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                  pip install --upgrade pip
                  pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}