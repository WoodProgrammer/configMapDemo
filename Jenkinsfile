pipeline {
  environment {
    registry = "nkudatascience123/docker-test"
    registryCredential = "dockerhub"
  }
  agent any
  stages {
    stage("Cloning Git") {
      steps {
        git "https://github.com/WoodProgrammer/configMapDemo.git"
      }
    }
    stage("Building image") {
      steps{
        script {
          docker.build registry + ":latest"
        }
      }
    }
  }
}
