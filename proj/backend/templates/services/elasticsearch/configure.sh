#!/bin/bash

# Usage: ./configure.sh

echo "Configuring Elasticsearch"

docker build -t elasticsearch ./services/elasticsearch
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300   -e "discovery.type=single-node" elasticsearch
