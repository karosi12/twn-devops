def incrementVersion() {
    echo "Increment app version..."

    dir("jenkins/jenkins-exercises/app/") {
        sh "npm version minor"

        // read the updated version from the package.json file
        // Note: install pipline utility steps plugin
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
    echo "success - docker build and push"
}

def deployImage(){
    sh "ls -la"
    def shellCmd = "bash ./server-cmds.sh ${IMAGE_NAME} ${DOCKER_HUB_ID}"
    def ec2Instance = "ec2-user@18.197.112.185"

    sshagent(['ec2-server-key']) {
        sh "scp -o StrictHostKeyChecking=no jenkins/jenkins-exercises/server-cmds.sh ${ec2Instance}:/home/ec2-user"
        sh "scp -o StrictHostKeyChecking=no jenkins/jenkins-exercises/docker-compose.yaml ${ec2Instance}:/home/ec2-user"
        sh "ssh -o StrictHostKeyChecking=no ${ec2Instance} ${shellCmd}"
    }     
    echo "success - Deployed"
}

def commitVersionUpdate(){
    withCredentials([usernamePassword(credentialsId: 'github-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
        // git config here for the first time run
        sh 'git config --global user.email  "jenkins@example.com"'
        sh 'git config --global user.name $USER'
        sh 'git remote set-url origin https://$USER:$PASS@github.com/$USER/twn-devops.git'
        sh 'git add .'
        sh 'git commit -m "ci: version bump"'
        sh 'git push origin HEAD:ft-jenkins'
    }

}

return this
