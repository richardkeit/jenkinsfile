node {
    stage('Build'){
       
        sh "zip test.zip *"
        step([$class: 'ArtifactArchiver', artifacts: 'test.zip', fingerprint: true])
        checkout([$class: 'GitSCM', branches: [[name: '*/develop']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/richardkeit/jenkinsfile.git']]])
    }
    
    stage('Test'){
         isUnix()
         sleep 30
    }
    
    
}