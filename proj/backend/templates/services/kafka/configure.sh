#!/bin/bash

# Usage: ./configure.sh zookeeper_ip

ZOOKEEPER_IP=$1

echo "Configuring Kafka with Zookeeper IP: $ZOOKEEPER_IP"

docker build -t kafka ./services/kafka
docker run -d --name kafka -p 9092:9092   -e KAFKA_ZOOKEEPER_CONNECT=$ZOOKEEPER_IP:2181   -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092   kafka
