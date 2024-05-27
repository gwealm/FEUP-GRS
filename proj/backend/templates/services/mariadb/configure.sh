#!/bin/bash

# Usage: ./configure.sh root_password

ROOT_PASSWORD=$1

echo "Configuring MariaDB with root password: $ROOT_PASSWORD"

docker build -t mariadb ./services/mariadb
docker run -d --name mariadb -p 3306:3306   -e MYSQL_ROOT_PASSWORD=$ROOT_PASSWORD   mariadb
