# save the artifact details in a json file

curl -u admin:password -X GET 'http://52.200.253.124:8081/service/rest/v1/components?repository=npm-private&sort=version' | jq "." > artifact.json

# grab the download url from the saved artifact details using 'jq' json processor tool
artifactDownloadUrl=$(jq '.items[0].assets[0].downloadUrl' artifact.json --raw-output)

fileName=$(jq '.items[0].name' artifact.json --raw-output)
version=$(jq '.items[0].version' artifact.json --raw-output)
extension=".tgz"
projectName=${fileName}-${version}${extension}

# fetch the artifact with the extracted download url using 'wget' tool
wget --http-user=admin --http-password=password $artifactDownloadUrl

echo $projectName
tar xzf $projectName

rm -rf $projectName


cd package
npm install 
node server.js &