pipeline{

    agent any

    environment {
	    IMAGE_NAME = 'mynginx'
        CONTAINER_PORT = 80
        NGINX_PORT = 80
        SECRET_VAR = credentials('nginx_var')
    }
    stages{
      stage('Prepare'){
        steps{
          echo "SECRET_VAR is: ${env.SECRET_VAR}"
        }
      }
      stage('Build') {
            steps {
              scripts{
                docker.build("NGINX_IMAGE_NAME")
              }
            }
        }
      stage('Deploy') {
            steps {
              scripts{
                echo "docker running Nginx reverse-proxy container; pwd"
                docker.image("${IMAGE_NAME}").run("-d -p ${CONTAINER_PORT}:${NGINX_PORT} --name ${IMAGE_NAME}-web")
              }
            }
        }
    }
}
