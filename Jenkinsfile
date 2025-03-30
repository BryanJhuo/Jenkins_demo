pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/BryanJhuo/Jenkins_demo.git', branch: 'main'
            }
        }

        stage('Unit Tests') {
            agent {
                docker { image 'python:3.12'}
            }
            steps {
                sh '''
                  echo "[🧪 Unit Test Started...]"
                  pip install -r requirements.txt || pip install pytest
                  PYTHONPATH=src pytest
                '''
            }
        }

        stage('Fuzz Test (AFL++ Python)') {
            steps {
                sh '''
                  docker build -t afl-python-fuzz ./fuzz
                  timeout 30s docker run --rm afl-python-fuzz
                '''
            }
        }
    }
}