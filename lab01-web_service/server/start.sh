#!/bin/bash
/sbin/ip route replace default via 10.0.2.6
nginx -g "daemon off;"
