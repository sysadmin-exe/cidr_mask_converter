pipeline {
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

    stage('Build Image') {
     
      steps {
        sh 'echo "docker build phase"'
        sh 'docker build  -f Dockerfile -t cheedee/cidr:cidr_app.V${BUILD_NUMBER} .'
      }
    }

stage('Deploy Docker Image') {
            steps {
                script {
                 withCredentials([string(credentialsId: 'docker', variable: 'dockerhubpwd')]) {
                    sh 'docker login -u cheedee -p ${dockerhubpwd}'
                 }  
                 sh 'docker push cheedee/cidr:cidr_app.V${BUILD_NUMBER} .'
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
