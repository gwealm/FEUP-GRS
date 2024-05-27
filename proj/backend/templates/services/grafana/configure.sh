#!/bin/bash

# Usage: ./configure.sh

echo "Configuring Grafana"

docker build -t grafana ./services/grafana
docker run -d --name grafana -p 3000:3000 grafana
