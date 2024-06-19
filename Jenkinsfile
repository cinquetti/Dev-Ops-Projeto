pipeline {
    agent any

    environment {
        DOCKER_VERSION = '20.10.8'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/cinquetti/Dev-Ops-Projeto.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Construir a imagem Docker a partir do Dockerfile na pasta docker/
                    sh 'docker-compose build'
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Rodar testes
                    sh 'docker-compose run app'
                }
            }
        }
    }
}




