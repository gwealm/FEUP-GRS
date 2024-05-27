#!/bin/bash

# Usage: ./configure.sh

echo "Configuring Zookeeper"

docker build -t zookeeper ./services/zookeeper
docker run -d --name zookeeper -p 2181:2181 zookeeper
