#!/bin/bash
docker kill `docker ps -aq`
docker rm `docker ps -aq`
docker system prune -f --volumes
docker image prune -af
