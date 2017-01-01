node {
  step([$class: 'WsCleanup'])
}

def build_tag_var = "${env.BUILD_TAG}"
def build_pipeline_name = "${env.JOB_NAME}"
def server = Artifactory.server '1'

println build_tag_var
println build_pipeline_name
node {
    
    stage('Build'){
    	println "ensure clean workspace"
    	sh "rm -rfv ${env.WORKSPACE}/*"
    	checkout([$class: 'GitSCM', branches: [[name: '*/develop']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/richardkeit/jenkinsfile.git']]])
        sh "tar -cvf ${build_tag_var}.tar *.txt *.md *.py"
        step([$class: 'ArtifactArchiver', artifacts: "${build_tag_var}.tar", fingerprint: true])
        
        
        def uploadSpec = """{
          "files": [
            {
              "pattern": "${build_tag_var}.tar",
              "target": "gdss-generic/${build_pipeline_name}/${build_tag_var}.tar",
              "props": "build_info=${build_tag_var};test=1"

            }
          ]
        }"""
        server.upload(uploadSpec)
        println "deleting artifact from workspace"
        sh "rm -rfv ${build_tag_var}.tar"   

        println "Uploading build info"
        def buildInfo = Artifactory.newBuildInfo()
        buildInfo.env.capture = true
        server.publishBuildInfo(buildInfo)

    }
    stage('Test'){
         isUnix()
         sleep 5

        def downloadSpec = """{
          "files": [
            {
              "pattern": "gdss-generic/${build_pipeline_name}/${build_tag_var}.tar",
              "target": "temp/"

            }
          ]
        }"""
        server.download(downloadSpec)   
        sh "mkdir -p ${env.WORKSPACE}/deploy"     
        sh "tar --ignore-command-error -xf ${env.WORKSPACE}/temp/${build_pipeline_name}/${build_tag_var}.tar -C ${env.WORKSPACE}/deploy "
    

    	println "running some mock tests in parallel"
           parallel (
            phase1: { sh "python -m py_compile ${env.WORKSPACE}/deploy/app.py " },
            phase2: { sh "echo phase2 testing" }
            )
                
        
        
    }
    
    
}