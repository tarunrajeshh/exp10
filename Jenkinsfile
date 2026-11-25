pipeline{
  agent any
  environment {
    REGISTRY = "localhost:5001"
    IMAGE_NAME = "student-demo-app"
  }
  stages{
    stage('1.CHeckout Code'){
      steps{
        checkout scm
      }
    }
