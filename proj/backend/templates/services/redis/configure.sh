#!/bin/bash

# Usage: ./configure.sh

echo "Configuring Redis"

docker build -t redis ./services/redis
docker run -d --name redis -p 6379:6379 redis
