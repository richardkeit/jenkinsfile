// As testing will be done between local and work instances, using vars to easily define the artifactory hosts

def apro_host = "1"


if (apro_host == "1") {
	println "this is local instance, assigning folders accordingly"
	def artefact_dir = "test"
	
}

if (apro_host == "2") {
	println "this is a corporate instance, assign folders accordingly"
	def artefact_dir = "test"
	if (artefact_dir == "test") {
		println "this shouldn't be test - should be platform specific\r\nexiting this now"
		System.exit(5)
		
	}

}

println "This is the directory" + artefact_dir

node {
  step([$class: 'WsCleanup'])
}

def build_tag_var = "${env.BUILD_TAG}"
def build_pipeline_name = "${env.JOB_NAME}"
def server = Artifactory.server apro_host

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
              "target": "${artefact_dir}/${build_pipeline_name}/${build_tag_var}.tar",
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

        println "downloading artifact"
        def downloadSpec = """{
          "files": [
            {
              "pattern": "${artefact_dir}/${build_pipeline_name}/${build_tag_var}.tar",
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