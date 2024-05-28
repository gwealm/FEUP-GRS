#!/bin/bash

iptables -t nat -A POSTROUTING --out-interface eth0 -j MASQUERADE

# Should we restart the service ???

echo 1 > /proc/sys/net/ipv4/ip_forward