#https://wiki.ubuntu.com/JonathanFerguson/Quagga

systemctl start zebra
systemctl start ospfd
systemctl start bgpd
/root/sleep.sh

