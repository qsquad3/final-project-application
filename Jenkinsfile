pipeline {

  options {
    buildDiscarder(logRotator(numToKeepStr: '10'))
    ansiColor('xterm')
    timestamps()
    timeout(time: 20, unit: 'MINUTES')
  }

  agent {
    dockerfile { filename 'Dockerfile.build' }
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build') {
      steps {
        script {
          sh """
          pip install -r requirements.txt
          """
        }
      }
    }

    stage('Lint') { // Run pylint against your code
      steps {
        script {
          sh """
          pylint **/*.py
          """
        }
      }
    }

    stage('Test') {
      steps {
        sh 'python test.py'
      } 
    }

    post {
    failure {
      script {
        msg = "Build error for ${env.JOB_NAME} ${env.BUILD_NUMBER} (${env.BUILD_URL})"
        
        slackSend message: msg, channel: env.SLACK_CHANNEL
        }
      }
    }
  }
}