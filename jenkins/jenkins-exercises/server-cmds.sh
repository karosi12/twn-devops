export IMAGE=$1
export DOCKER_HUB_ID=$2
docker-compose -f docker-compose.yaml up --detach
echo "success"

