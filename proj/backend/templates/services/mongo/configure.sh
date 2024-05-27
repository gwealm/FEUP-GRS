#!/bin/bash

# Usage: ./configure.sh

echo "Configuring MongoDB"

docker build -t mongo ./services/mongo
docker run -d --name mongo -p 27017:27017 mongo
