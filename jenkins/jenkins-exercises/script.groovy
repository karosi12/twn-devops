def incrementVersion() {
    echo "Increment app version..."
    dir("app") {
        # update application version in the package.json file with one of these release types: patch, minor or major
        # this will commit the version update
        sh "npm version minor"

        # read the updated version from the package.json file
        def packageJson = readJSON file: 'package.json'
        def version = packageJson.version

        # set the new version as part of IMAGE_NAME
        env.IMAGE_NAME = "$version-$BUILD_NUMBER"
    }

    # alternative solution without Pipeline Utility Steps plugin: 
    # def version = sh (returnStdout: true, script: "grep 'version' package.json | cut -d '\"' -f4 | tr '\\n' '\\0'")
    # env.IMAGE_NAME = "$version-$BUILD_NUMBER"

} 

def buildAndPushDockerImage(){
    withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]){
        sh "docker build -t ${DOCKER_HUB_ID}/myapp:${IMAGE_NAME} ."
        sh 'echo $PASS | docker login -u $USER --password-stdin'
        sh "docker push ${DOCKER_HUB_ID}/myapp:${IMAGE_NAME}"
    }
}

return this