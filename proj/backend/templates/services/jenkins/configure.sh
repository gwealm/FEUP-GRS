#!/bin/bash

# Usage: ./configure.sh admin_password

ADMIN_PASSWORD=$1

echo "Configuring Jenkins with admin password: $ADMIN_PASSWORD"

docker build -t jenkins ./services/jenkins
docker run -d --name jenkins -p 8080:8080 -p 50000:50000   -v jenkins_home:/var/jenkins_home   -e JENKINS_OPTS="--argumentsRealm.passwd.admin=$ADMIN_PASSWORD --argumentsRealm.roles.user=admin"   jenkins
