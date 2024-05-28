FROM internetsystemsconsortium/bind9:9.16

RUN apt update && apt install -y vim iproute2 iputils-ping tcpdump iptables dnsutils curl apache2-utils traceroute

COPY sleep.sh /root/sleep.sh
