pipeline {

  options {
    skipDefaultCheckout(true)
    buildDiscarder(logRotator(numToKeepStr: '10'))
    timestamps()
  }

  agent any

  environment {
    NEW_VERSION = '1.0.0'
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build') {
      agent {
        docker {
          image 'python:2-alpine'
        }
      }
      steps {
        echo "Building"
        echo "Building version ${NEW_VERSION}"
        sh 'python -m py_compile app/app.py'
      }
    }

    stage('Lint') {
      steps {
        echo "Linting"
        sh 'pylint **/*.py'
      }
    }

    stage('Test') {
      steps {
        echo "Testing the application"
        sh 'python test.py'
      } 
    }

    stage('Deploy')
    {
      steps {
        echo "Deploying the application"
      }
    }
  }

  post {
    always {
      echo 'The pipeline completed'
      junit allowEmptyResults: true, testResults:'**/test_reports/*.xml'
    }
    success {
      echo "Flask Application Up and running!!"
    }
    failure {
      echo 'Build stage failed'
      error('Stopping early…')
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