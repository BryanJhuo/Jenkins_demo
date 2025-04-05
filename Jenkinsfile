pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/BryanJhuo/Jenkins_demo.git', branch: 'main'
            }
        }

        stage('Build OSS-Fuzz image') {
            steps {
                sh '''
                  docker build -t ossfuzz-demo -f fuzz/Dockerfile .
                '''
            }
        }

        stage('Run local Fuzzing') {
            steps {
                sh '''
                  docker run --rm ossfuzz-demo
                '''
            }
        }
    }
}