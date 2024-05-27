#!/bin/bash

# Usage: ./configure_service.sh service_name variable1 variable2 ...

SERVICE_NAME=$1
shift

case $SERVICE_NAME in
  gitlab)
    ./services/gitlab/configure.sh "$@"
    ;;
  redis)
    ./services/redis/configure.sh "$@"
    ;;
  nginx)
    ./services/nginx/configure.sh "$@"
    ;;
  mongo)
    ./services/mongo/configure.sh "$@"
    ;;
  elasticsearch)
    ./services/elasticsearch/configure.sh "$@"
    ;;
  *)
    echo "Service $SERVICE_NAME is not recognized."
    ;;
esac
