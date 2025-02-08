pipeline {
    agent any
    environment {
        DOCKER_REGISTRY = "159.203.123.66:8090"  // Repositorio de Nexus actualizado
        DOCKER_IMAGE = "image_fastapi"           // Nombre de la imagen
        DOCKER_TAG = "latest"                    // Tag de la imagen
        SERVER_USER = "root"                      // Usuario del servidor
        SERVER_IP = "159.203.123.66"              // Dirección IP del servidor
        NEXUS_USER = "admin"                      // Usuario de Nexus 
        NEXUS_PASS = "PedroJ85"                   // Contraseña de Nexus 
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
                sh "docker build -t $DOCKER_REGISTRY/$DOCKER_IMAGE:$DOCKER_TAG ."
            }
        }
        stage('Login to Nexus') {
            steps {
                echo "🔑 Autenticando en Nexus..."
                sh "echo '$NEXUS_PASS' | docker login -u $NEXUS_USER --password-stdin $DOCKER_REGISTRY"
            }
        }
        stage('Push to Nexus') {
            steps {
                echo "📤 Subiendo imagen a Nexus..."
                sh "docker push $DOCKER_REGISTRY/$DOCKER_IMAGE:$DOCKER_TAG"
            }
        }
        stage('Deploy to Server') {
            steps {
                echo "🚀 Desplegando aplicación en el servidor..."
                script {
                    sshagent(credentials: ['ssh-server-credentials']) {
                        sh """
                        ssh -o StrictHostKeyChecking=no $SERVER_USER@$SERVER_IP << 'ENDSSH'
                        echo "📥 Descargando la última imagen de Docker..."
                        docker pull $DOCKER_REGISTRY/$DOCKER_IMAGE:$DOCKER_TAG

                        echo "🔍 Verificando si el contenedor $DOCKER_IMAGE está en ejecución..."
                        if [ \$(docker ps -q -f name=$DOCKER_IMAGE) ]; then
                            echo "🛑 Deteniendo el contenedor en ejecución..."
                            docker stop $DOCKER_IMAGE
                        fi

                        echo "🗑️ Eliminando contenedor antiguo (si existe)..."
                        docker rm -f $DOCKER_IMAGE || true

                        echo "🔍 Verificando si el puerto 5000 está en uso..."
                        if lsof -i :5000 | grep LISTEN; then
                            echo "⚠️ El puerto 5000 está en uso. Liberándolo..."
                            fuser -k 5000/tcp
                            sleep 3
                        fi

                        echo "🏃‍♂️ Iniciando nuevo contenedor..."
                        docker run -d --restart unless-stopped --name $DOCKER_IMAGE -p 5000:5000 $DOCKER_REGISTRY/$DOCKER_IMAGE:$DOCKER_TAG

                        echo "✅ Despliegue completado exitosamente!"
                        exit
                        ENDSSH
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
