#!/bin/bash

# Usage: ./configure.sh external_url

EXTERNAL_URL=$1

echo "Configuring GitLab with external URL: $EXTERNAL_URL"

docker build -t gitlab ./services/gitlab
docker run -d --name gitlab --hostname gitlab.example.com \
  -p 8929:8929 -p 2224:22 \
  -v gitlab_config:/etc/gitlab \
  -v gitlab_logs:/var/log/gitlab \
  -v gitlab_data:/var/opt/gitlab \
  -e GITLAB_OMNIBUS_CONFIG="external_url '$EXTERNAL_URL'" \
  gitlab

docker exec -it gitlab gitlab-ctl reconfigure
