def incrementVersion() {
    echo "Increment app version..."

    dir("jenkins/jenkins-exercises/app/") {
        sh "npm version minor"

        // # read the updated version from the package.json file
        def packageJson = readJSON file: 'package.json'
        def version = packageJson.version
        // # set the new version as part of IMAGE_NAME
        env.IMAGE_NAME = "$version-$BUILD_NUMBER"
        echo env.IMAGE_NAME
    }
       
    /** 
     alternative solution without Pipeline Utility Steps plugin: 
    def version = sh (returnStdout: true, script: "grep 'version' package.json | cut -d '\"' -f4 | tr '\\n' '\\0'")
    env.IMAGE_NAME = "$version-$BUILD_NUMBER"
    */
} 

def runTest() {
    // enter app directory, because that's where package.json and tests are located
    dir("jenkins/jenkins-exercises/app") {
        //  install all dependencies needed for running tests
        sh "npm install"
        sh "npm run test"
    } 
}

def buildAndPushDockerImage(){
    dir("jenkins/jenkins-exercises") {
        sh "ls -la"
        withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]){
            sh "docker build -t ${DOCKER_HUB_ID}/myapp:${IMAGE_NAME} ."
            sh 'echo $PASS | docker login -u $USER --password-stdin'
            sh "docker push ${DOCKER_HUB_ID}/myapp:${IMAGE_NAME}"
        }
    }
    echo "buildAndPushDockerImage"
}

def commitVersionUpdate(){
    withCredentials([usernamePassword(credentialsId: 'github-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
        // git config here for the first time run
        sh 'git config --global user.email "jenkins@example.com"'
        sh 'git config --global user.name $USER'
        sh 'git remote set-url origin https://github.com/karosi12/twn-devops.git'
        sh 'git add .'
        sh 'git commit -m "ci: version bump"'
        sh 'git push origin HEAD:ft-jenkins'
    }

}

return this
