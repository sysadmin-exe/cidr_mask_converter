pipeline {
  agent any

  stages {

    stage('PR ONLY - Install App Dependencies') {
      when {
        not {
          anyOf{
            branch 'master'
          }
        }
      }
      steps {
        _sh """
        echo 'PR - installing app build requirements'
        cd cidr_convert_api/python
        pip install virtualenv
        virtualenv victor
        ls
        source victor/bin/activate
        pip install -r requirements.txt
        """
      }
    }

    stage('PR ONLY - test') {
      when {
        not {
          anyOf{
            branch 'master'
          }
        }
      }
      steps {
        sh 'echo "PR - testing the code"'
        sh 'python cidr_convert_api/python/tests.py'
      }  
    }

    stage('PR ONLY - Build Image') {
      when {
        not {
          anyOf{
            branch 'master'
          }
        }
      }
      steps {
        sh 'echo "PR - docker build phase"'
        sh 'docker build  -f cidr_convert_api/python/Dockerfile -t wizelinedevops/victor-efedi:cidr_app.V${BUILD_NUMBER} .'
        sh 'docker rmi wizelinedevops/victor-efedi:cidr_app.V${BUILD_NUMBER}'
      }
    }

    stage('Install App Dependencies') {
        when {
          anyOf {
            branch 'master'
          }
        }
        steps {
          _sh """
          echo 'installing app build requirements'
          cd cidr_convert_api/python
          pip install virtualenv
          virtualenv victor
          ls
          source victor/bin/activate
          pip install -r requirements.txt
          """
        }
      }

    stage('test') {
      when {
        anyOf {
          branch 'master'
        }
      }
      steps {
        sh 'echo "testing the code"'
        sh 'python cidr_convert_api/python/tests.py'
      }  
    }

    stage('Build Image') {
      when {
        anyOf {
          branch 'master'
        }
      }
      steps {
        sh 'echo "docker build phase"'
        sh 'docker build  -f cidr_convert_api/python/Dockerfile -t wizelinedevops/victor-efedi:cidr_app.V${BUILD_NUMBER} .'
      }
    }

    stage('Push Image') {
      when {
        anyOf {
          branch 'master'
        }
      }
      steps{
        sh 'echo "Pushing Image to Docker Hub"'
        sh 'docker push wizelinedevops/victor-efedi:cidr_app.V${BUILD_NUMBER}'
        sh 'docker rmi wizelinedevops/victor-efedi:cidr_app.V${BUILD_NUMBER}'
      }
    }   

    stage('Deploy to Dev Kubernetes') {
      environment {
          KUBECONFIG = credentials('KUBECONFIG')
      }
      when {
        anyOf {
          branch 'master'
        }
      }
      steps {
        _sh """
          kubectl --kubeconfig=$KUBECONFIG --namespace=$DEV_ENV --record deployment/api set image deployment/api api=wizelinedevops/victor-efedi:cidr_app.V${BUILD_NUMBER}
            """
      }
    }

    stage('Deploy to Staging Kubernetes') {
    input{
    message "Do you want to proceed for staging deployment?"
    }
      environment {
          KUBECONFIG = credentials('KUBECONFIG')
      }
      when {
        anyOf {
          branch 'master'
        }
      }
      steps {
        _sh """
          kubectl --kubeconfig=$KUBECONFIG --namespace=$STAGE_ENV --record deployment/api set image deployment/api api=wizelinedevops/victor-efedi:cidr_app.V${BUILD_NUMBER}
            """
      }
    }

    stage('Deploy to Production Kubernetes') {
    input{
    message "Do you want to proceed for production deployment?"
    }
      environment {
          KUBECONFIG = credentials('KUBECONFIG')
      }
      when {
        anyOf {
          branch 'master'
        }
      }
      steps {
        _sh """
          kubectl --kubeconfig=$KUBECONFIG --namespace=$PROD_ENV --record deployment/api set image deployment/api api=wizelinedevops/victor-efedi:cidr_app.V${BUILD_NUMBER}
            """
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