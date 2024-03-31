#!/bin/bash
docker kill `docker ps -aq`
docker rm `docker ps -aq`
docker system prune -f --volumes
docker image prune -af

sleep 4

docker compose \
    -f docker-compose.org1.yml \
    -f docker-compose.org2.yml \
    up