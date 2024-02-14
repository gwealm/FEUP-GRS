#!/bin/bash
/sbin/ip route replace default via 10.0.3.1

## NAT ##

# Is this really relevant??
# iptables -t nat --delete-chain

iptables -t nat -A POSTROUTING --out-interface eth1 -j MASQUERADE
iptables -A FORWARD --in-interface eth2 -j ACCEPT
iptables -A FORWARD --in-interface eth3 -j ACCEPT

# Should we restart the service ???

echo 1 > /proc/sys/net/ipv4/ip_forward