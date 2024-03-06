#!/bin/bash

# public network
sudo docker network create public_net --subnet=172.31.255.0/24 --gateway=172.31.255.254

# org1 nets
sudo docker network create org1_int1_net --subnet=10.0.1.0/29 --gateway=10.0.1.1
sudo docker network create org1_int2_net --subnet=10.0.1.8/29 --gateway=10.0.1.9
sudo docker network create org1_int3_net --subnet=10.0.1.16/29 --gateway=10.0.1.17
sudo docker network create org1_pub1_net --subnet=172.16.123.128/28 --gateway=172.16.123.129
sudo docker network create org1_pub2_net --subnet=172.16.123.144/28 --gateway=172.16.123.145



# org1 routers
echo ">>>>1"
sudo docker run -d --net org1_int1_net --ip 10.0.1.2 \
    -v /home/gors/quagga/zebra.conf:/etc/quagga/zebra.conf \
    -v /home/gors/quagga/ospfd.conf:/etc/quagga/ospfd.conf \
    -v /home/gors/quagga/start.sh:/root/start.sh \
    --cap-add=NET_ADMIN  --privileged --name org1_router1 netubuntu 
sudo docker network connect org1_int2_net org1_router1 --ip 10.0.1.10
sudo docker network connect public_net org1_router1 --ip 172.31.255.253
sudo docker exec org1_router1 /bin/bash -c 'ip r del default via 10.0.1.1'
sudo docker exec org1_router1 /bin/bash -c 'ip r add default via 172.31.255.1'

echo ">>>>2"
sudo docker run -d --net org1_int2_net --ip 10.0.1.11 \
    -v /home/gors/quagga/zebra.conf:/etc/quagga/zebra.conf \
    -v /home/gors/quagga/ospfd.conf:/etc/quagga/ospfd.conf \
    -v /home/gors/quagga/start.sh:/root/start.sh \
    --cap-add=NET_ADMIN --privileged --name org1_router2 netubuntu 
sudo docker network connect org1_int3_net org1_router2 --ip 10.0.1.18
sudo docker network connect org1_pub2_net org1_router2 --ip 172.16.123.158
sudo docker exec org1_router2 /bin/bash -c 'ip r del default via 10.0.1.9'
echo ">>>>3"
sudo docker run -d --net org1_int1_net --ip 10.0.1.3 \
    -v /home/gors/quagga/zebra.conf:/etc/quagga/zebra.conf \
    -v /home/gors/quagga/ospfd.conf:/etc/quagga/ospfd.conf \
    -v /home/gors/quagga/start.sh:/root/start.sh \
    --cap-add=NET_ADMIN --privileged --name org1_router3 netubuntu 
sudo docker network connect org1_int3_net org1_router3 --ip 10.0.1.19
sudo docker network connect org1_pub1_net org1_router3 --ip 172.16.123.142
sudo docker exec org1_router3 /bin/bash -c 'ip r del default via 10.0.1.1'

echo ">>>>server1"

sudo docker run -d --net org1_pub1_net --ip 172.16.123.130 --cap-add=NET_ADMIN --name org1_server1 netubuntu 
sudo docker exec org1_server1 /bin/bash -c 'ip r del default via 172.16.123.129'
sudo docker exec org1_server1 /bin/bash -c 'ip r add default via 172.16.123.142'
echo ">>>>server2"
sudo docker run -d --net org1_pub2_net --ip 172.16.123.146 --cap-add=NET_ADMIN --name org1_server2 netubuntu 
sudo docker exec org1_server2 /bin/bash -c 'ip r del default via 172.16.123.145'
sudo docker exec org1_server2 /bin/bash -c 'ip r add default via 172.16.123.158'

# docker host (target)
sudo ip r d 172.16.123.128/28
sudo ip r d 172.16.123.144/28
sudo ip r a 172.16.123.128/28 via 172.31.255.253
sudo ip r a 172.16.123.144/28 via 172.31.255.253
