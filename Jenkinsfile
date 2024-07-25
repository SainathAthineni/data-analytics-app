pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                bat 'pytest'
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
