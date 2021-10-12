pip3eline {
  agent any

  stages {
// stage('PR ONLY - Install App Dependencies') {
//       
//       steps {
//         _sh """
//         echo 'installing app build requirements'
//         cd cidr_convert_api/python
//         pip3 install virtualenv
//         virtualenv victor
//         ls
//         source victor/bin/activate
//         pip3 install -r requirements.txt
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
          pip3 install virtualenv
          virtualenv victor
          ls
          source victor/bin/activate
          pip3 install -r requirements.txt
          """
        }
      }

    stage('test') {
      
      steps {
        sh 'echo "testing the code"'
        sh 'python cidr_convert_api/python/tests.py'
      }  
    }

    stage('Build Image') {
     
      steps {
        sh 'echo "docker build phase"'
        sh 'docker build  -f cidr_convert_api/python/Dockerfile -t cheedee/cidr:cidr_app.V${BUILD_NUMBER} .'
      }
    }

    stage('Push Image') {
      
      steps{
        sh 'echo "Pushing Image to Docker Hub"'
        sh 'docker push cheedee/cidr:cidr_app.V${BUILD_NUMBER}'
        sh 'docker rmi cheedee/cidr:cidr_app.V${BUILD_NUMBER}'
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