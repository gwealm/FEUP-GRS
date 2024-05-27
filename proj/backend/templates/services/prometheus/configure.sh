#!/bin/bash

# Usage: ./configure.sh

echo "Configuring Prometheus"

docker build -t prometheus ./services/prometheus
docker run -d --name prometheus -p 9090:9090 prometheus
