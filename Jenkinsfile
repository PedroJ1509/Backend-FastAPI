pipeline {
    agent any
    environment {
        DOCKER_REGISTRY = "159.203.123.66:8090"
        DOCKER_IMAGE = "image_fastapi"
        DOCKER_TAG = "latest"
        SERVER_USER = "root"
        SERVER_IP = "159.203.123.66"
        NEXUS_USER = "admin"
        NEXUS_PASS = "PedroJ85"
    }
    stages {
        stage('Checkout') {
            steps {
                echo "📥 Clonando código fuente desde GitHub..."
                git branch: 'develop', credentialsId: 'github-credentials', url: 'https://github.com/PedroJ1509/Backend-FastAPI.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo "🔨 Construyendo imagen Docker..."
                bat "docker build -t %DOCKER_REGISTRY%/%DOCKER_IMAGE%:%DOCKER_TAG% ."
            }
        }
        stage('Login to Nexus') {
            steps {
                echo "🔑 Autenticando en Nexus..."
                bat "echo %NEXUS_PASS% | docker login -u %NEXUS_USER% --password-stdin %DOCKER_REGISTRY%"
            }
        }
        stage('Push to Nexus') {
            steps {
                echo "📤 Subiendo imagen a Nexus..."
                bat "docker push %DOCKER_REGISTRY%/%DOCKER_IMAGE%:%DOCKER_TAG%"
            }
        }
        stage('Deploy to Server') {
            steps {
                echo "🚀 Desplegando aplicación en el servidor..."
                script {
                    sshagent(credentials: ['ssh-server-credentials']) {
                        bat """
                        ssh -o StrictHostKeyChecking=no %SERVER_USER%@%SERVER_IP% ^
                        "docker pull %DOCKER_REGISTRY%/%DOCKER_IMAGE%:%DOCKER_TAG% && ^
                        docker stop %DOCKER_IMAGE% || true && ^
                        docker rm %DOCKER_IMAGE% || true && ^
                        docker run -d --restart unless-stopped --name %DOCKER_IMAGE% -p 5000:5000 %DOCKER_REGISTRY%/%DOCKER_IMAGE%:%DOCKER_TAG%"
                        """
                    }
                }
            }
        }
    }
    post {
        success {
            echo "🎉 Pipeline completado exitosamente!"
        }
        failure {
            echo "🚨 ERROR: Algo falló en el pipeline, revisa los logs!"
        }
    }
}
