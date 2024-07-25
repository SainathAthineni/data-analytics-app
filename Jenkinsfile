pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}/data-analytics-app"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                bat 'call venv\\Scripts\\activate && pytest'
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    bat 'docker build -t my-python-app:latest .'
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    bat 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
