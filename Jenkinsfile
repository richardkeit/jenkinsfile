node {
    stage('Build'){
        def build_tag_var = ${env.BUILD_TAG}
        sh "zip ${build_tag_var}.zip *"
        step([$class: 'ArtifactArchiver', artifacts: 'build_tag_var.zip', fingerprint: true])
        // checkout([$class: 'GitSCM', branches: [[name: '*/develop']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/richardkeit/jenkinsfile.git']]])
    }
    
    stage('Test'){
         isUnix()
         sleep 30
    }
    
    
}