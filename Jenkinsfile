pipeline {
    environment{
       registry = "swaydevstan/cidrproj"
       registryCredential = 'dockerhub'
       dockerImage = ''

    }
    agent any
    
    stages{

        stage ('Checkout branch'){
            steps {
                script{
                    checkout([$class: 'GitSCM', branches: [[name: 'develop-stanley']], extensions: [], userRemoteConfigs: [[credentialsId: '001git', url: 'https://github.com/sysadmin-exe/cidr_mask_converter.git']]])
                }
          
            }
        }

        stage ('Install App dependencies'){
            steps{
                withPythonEnv('python3.7'){
                //uses the Pyenv Pipeline Plugin method to create the virtual environment and install requirements
                _sh """
                echo 'installing app build requirements'
                pip install -r requirements.txt
                """
                }
            }
        }

        stage ('Run tests'){
            steps {
              //used the Pyenv Pipeline Plugin method to create the virtual environment and run the test
                withPythonEnv('python3.7'){
                _sh """
                echo 'running test on the code'
                python tests.py
                """
                }
            }
        }

        stage ('Build Image'){
            steps{
              //uses the docker pipeline plugin entered the environments variable previously, which was used to build and push the images
                sh 'echo "building docker image"'
                script{
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    //remove image from jenkins server
                    sh 'docker rmi  ${dockerImage.imageName()} -f'
                }
            }
        }

        stage ('Push Image'){
           steps{
                sh 'echo "Push docker image"'
                script {
                    docker.withRegistry( '', registryCredential ) { 
                    dockerImage.push() 
                    }    
                }
            }
        
        }

        stage ('Deploy to server'){
            steps{
              //uses the ssh agent to run the image on a container
                sh 'echo "Deploying to running Azure VM"'
                script{
                    def dockerRun = 'docker run -p 8000:8000 -d --name my-cidrproj swaydevstan/cidrproj:latest'
                    sshagent(['sshazurevm']) {
                     sh "ssh -o StrictHostKeyChecking=no stanley@linuxvmstan.eastus.cloudapp.azure.com ${dockerRun}"
                     }
                }

            } 
        }  
    }
}

def _sh (shell_command) {
  sh """
  #!/bin/bash -e
  $shell_command
  """
}
