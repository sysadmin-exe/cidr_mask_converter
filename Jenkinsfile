pipeline {
    environment{
       registry = "cheedee/cidr"
       registryCredential = 'docker'
       dockerImage = ''

    }
  agent any

  stages {
// stage('PR ONLY - Install App Dependencies') {
//       
//       steps {
//         _sh """
//         echo 'installing app build requirements'
//         cd cidr_convert_api/python
//         pip install virtualenv
//         virtualenv victor
//         ls
//         source victor/bin/activate
//         pip install -r requirements.txt
//         """
//       }
//     }

//     stage('PR ONLY - test') {
//       
//       steps {
//         sh 'echo "testing the code"'
//         sh 'python cidr_convert_api/python/tests.py'
//       }  
//     }

//     stage('PR ONLY - Build Image') {
//       
//       steps {
//         sh 'echo "docker build phase"'
//         sh 'docker build  -f cidr_convert_api/python/Dockerfile -t wizelinedevops/cidr:cidr_app.V${BUILD_NUMBER} .'
//         sh 'docker rmi wizelinedevops/cidr:cidr_app.V${BUILD_NUMBER}'
//       }
//     }

    stage('Install App Dependencies') {
        
        steps {
          _sh """
          echo 'installing app build requirements'
          pip install -r requirements.txt
          """
        }
      }
    stage('test') {
      
      steps {
        sh 'echo "testing the code"'
        sh 'python3 tests.py'
      }  
    }

        stage ('Build Image'){
            steps{
                sh 'echo "building docker image"'
                script{
                    dockerImage =  docker.build registry + ":latest"
                }
            }
        }

        stage ('Push Image'){
           steps{
                sh 'echo "Push docker image"'
                script{
                    docker.withRegistry( '', registryCredential ) { 
                    dockerImage.push() 
                    }    
                }
            }
        
        }
        stage ('Deploy to server'){
            steps{
              //uses the ssh agent to run the image on a container
                sh 'echo "Deploying to running VM"'
                script{
                    def dockerRun = 'docker run -p 8000:8000 -d --name cidrconverter cheedee/cidr:latest'
                    sshagent(['sshkey']) {
                     sh "ssh -o StrictHostKeyChecking=no chidi@172.31.146.172 ${dockerRun}"
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
