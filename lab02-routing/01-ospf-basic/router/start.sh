#!/bin/bash

#https://wiki.ubuntu.com/JonathanFerguson/Quagga
systemctl start zebra
systemctl start ospfd
/root/sleep.sh
