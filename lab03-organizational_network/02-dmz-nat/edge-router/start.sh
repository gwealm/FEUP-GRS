#!/bin/bash

ip route replace default via 172.31.255.254
# ip route add 10.0.0.0/16 via 172.16.123.142

# ## NAT ##
iptables -t nat -F; iptables -t filter -F

iptables -t nat -A POSTROUTING -s 10.0.0.0/16 -o eth1 -j MASQUERADE

iptables -P FORWARD DROP

iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -m state --state NEW -i eth0 -j ACCEPT
iptables -A FORWARD -m state --state NEW -i eth1 -d 172.16.123.128/28 -j ACCEPT