#!/bin/bash

# Usage: ./configure.sh db_host db_user db_password

DB_HOST=$1
DB_USER=$2
DB_PASSWORD=$3

echo "Configuring WordPress with DB Host: $DB_HOST, User: $DB_USER"

docker build -t wordpress ./services/wordpress
docker run -d --name wordpress -p 80:80   -e WORDPRESS_DB_HOST=$DB_HOST   -e WORDPRESS_DB_USER=$DB_USER   -e WORDPRESS_DB_PASSWORD=$DB_PASSWORD   wordpress
