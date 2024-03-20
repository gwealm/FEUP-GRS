#!/bin/bash

DOCKERINFO=$(curl -s --unix-socket /run/docker.sock http://docker/containers/$HOSTNAME/json)
ID=$(python3 -c "import sys, json; print(json.loads(sys.argv[1])[\"Name\"].split(\"_\")[-1])" "$DOCKERINFO")


echo "export SERVER_ID=$ID" >> ~/.bashrc
echo "export SERVER_ID=$ID" >> ~/id.txt
source ~/.bashrc


/sbin/ip route replace default via 10.0.2.254
nginx -g "daemon off;"


