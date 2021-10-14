pipeline {
  agent any

  stages {
    stage('PR ONLY - Install App Dependencies') {
        when {
            not {
              anyOf{
                branch 'develop-klerrie'
              }
            }
          }
          steps {
            _sh """
            echo 'installing app build requirements'
            pip install virtualenv
            virtualenv lehrie
            ls
            source lehrie/bin/activate
            pip install -r requirements.txt
            """
          }
        }

    stage('PR ONLY - test') {
      when {
        not {
          anyOf{
            branch 'develop-klerrie'
          }
        }
      }
      steps {
        sh 'echo "testing the code"'
        sh 'python tests.py'
      }  
    }

    stage('PR ONLY - Build Image') {
      when {
        not {
          anyOf{
            branch 'develop-klerrie'
          }
        }
      }
      steps {
        sh 'echo "docker build phase"'
        sh 'docker build  -f cidr_convert_api/python/Dockerfile -t wizelinedevops/lehrie-efedi:cidr_app.V${BUILD_NUMBER} .'
        sh 'docker rmi wizelinedevops/lehrie-efedi:cidr_app.V${BUILD_NUMBER}'
      }
    }

    stage('Install App Dependencies') {
        when {
          anyOf {
            branch 'develop-klerrie'
          }
        }
        steps {
          _sh """
          echo 'installing app build requirements'
          pip install virtualenv
          virtualenv lehrie
          ls
          source lehrie/bin/activate
          pip install -r requirements.txt
          """
        }
      }

    stage('test') {
      when {
        anyOf {
          branch 'develop-klerrie'
        }
      }
      steps {
        sh 'echo "testing the code"'
        sh 'python tests.py'
      }  
    }

    stage('Build Image') {
      when {
        anyOf {
          branch 'develop-klerrie'
        }
      }
      steps {
        sh 'echo "docker build phase"'
        sh 'docker build  -f cidr_convert_api/python/Dockerfile -t xxx/lehrie-efedi:cidr_app.V${BUILD_NUMBER} .'
      }
    }

    stage('Push Image') {
      when {
        anyOf {
          branch 'develop-klerrie'
        }
      }
      steps{
        sh 'echo "Pushing Image to Docker Hub"'
        sh 'docker push xxx/lehrie-efedi:cidr_app.V${BUILD_NUMBER}'
        sh 'docker rmi xxx/lehrie-efedi:cidr_app.V${BUILD_NUMBER}'
      }
    } 

    stage('Deploy to server') {
      when {
        anyOf {
          branch 'develop-klerrie'
        }
      }
      steps{
        //script to deploy the docker image goes here

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
