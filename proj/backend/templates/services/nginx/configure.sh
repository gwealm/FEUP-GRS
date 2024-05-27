#!/bin/bash

# Usage: ./configure.sh

echo "Configuring Nginx"

docker build -t nginx ./services/nginx
docker run -d --name nginx -p 80:80 -p 443:443 nginx
