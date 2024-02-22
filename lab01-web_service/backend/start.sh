#!/bin/bash
/sbin/ip route replace default via 10.0.2.6
nginx -g "daemon off;"


DOCKERINFO=$(curl -s --unix-socket /run/docker.sock http://docker/containers/$HOSTNAME/json)
ID=$(python3 -c "import sys, json; print(json.loads(sys.argv[1])[\"Name\"].split(\"_\")[-1])" "$DOCKERINFO")

# echo "This is node $ID"

export SERVER_ID=$ID
