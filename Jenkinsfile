pipeline {
    agent any

    environment {
        APP_NAME = "ShopSphere"
        PYTHON = "python3"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "===== Checking out source code ====="
                checkout scm
            }
        }

        stage('Repository Information') {
            steps {
                sh '''
                echo "Current Directory:"
                pwd

                echo "Repository Files:"
                ls -la
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                rm -rf venv
                python3 -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Python Version') {
            steps {
                sh '''
                . venv/bin/activate
                python --version
                pip --version
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

        stage('Workspace Information') {
            steps {
                sh '''
                echo "Workspace Size:"
                du -sh .

                echo "Disk Usage:"
                df -h
                '''
            }
        }
    }

    post {

        success {
            echo "================================="
            echo "Build Successful"
            echo "================================="
        }

        failure {
            echo "================================="
            echo "Build Failed"
            echo "================================="
        }

        always {
            cleanWs()
        }
    }
}
