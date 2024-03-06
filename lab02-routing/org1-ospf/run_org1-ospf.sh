#!/bin/bash
# https://www.nongnu.org/quagga/docs/quagga.html
export GORS_HOME=`pwd`
$GORS_HOME/docker-prune.sh
scp -r $GORS_HOME/org1-ospf/quagga gors-target:~/.
$GORS_HOME/runremote.sh gors-target $GORS_HOME/org1-ospf/org1-ospf.sh
