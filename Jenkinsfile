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
      echo "Building"
      agent {
        docker {
          image 'python:2-alpine'
        }
      }
      steps {
        sh 'python -m py_compile sources/add2vals.py sources/calc.py'
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