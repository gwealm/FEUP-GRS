#!/bin/bash
export GORS_HOME=`pwd`
scp -r $GORS_HOME/baseimage-cfg/baseimage/ gors-target:~/.
ssh gors-target 'sudo docker build --tag netubuntu:latest ~/baseimage'