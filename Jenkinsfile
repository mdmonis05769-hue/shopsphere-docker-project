pipeline {
    agent any

    stages {

        stage('Repository Information') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Python Version') {
            steps {
                sh '''
                . venv/bin/activate
                python --version
                '''
            }
        }

        stage('Static Code Check') {
            steps {
                sh '''
                . venv/bin/activate
                python -m py_compile app.py
                python -m py_compile db.py
                python -m py_compile cache.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t shopsphere:latest .
                '''
            }
        }

        stage('Docker Images') {
            steps {
                sh '''
                docker images
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
