pipeline {

  options {
    skipDefaultCheckout(true)
    buildDiscarder(logRotator(numToKeepStr: '10'))
    timestamps()
  }

  agent any

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build') {
      steps {
        echo 'Building'
        sh """
        pip install -r requirements.txt
        """
      }
    }

    stage('Lint') { // Run pylint against your code
      steps {
        echo 'Linting'
        sh """
        pylint **/*.py
        """
      }
    }

    stage('Test') {
      steps {
        echo 'Testing'
        sh 'python test.py'
      } 
    }
  }

  post {
    always {
      echo 'This will always run'
    }
    success {
      echo 'This will run only if successful'
    }
    failure {
      echo "Send e-mail, when failed"
    }
    unstable {
      echo 'This will run only if the run was marked as unstable'
    }
    changed {
      echo 'This will run only if the state of the Pipeline has changed'
      echo 'For example, if the Pipeline was previously failing but is now successful'
    }
  }
}