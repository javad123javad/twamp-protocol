pipeline {
  agent {
    label 'ecsAgent'
  }

  stages {
    
    stage('Install Requirements') {
      when {
        branch comparator: 'EQUALS', pattern: 'master'
      }
      steps {
        sh '''
        #!/bin/bash
        semantic-release publish   
        '''
      }
    }

  }
}
