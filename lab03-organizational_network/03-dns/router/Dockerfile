FROM ubuntu:20.04

RUN apt update && apt install -y vim iproute2 iputils-ping tcpdump iptables dnsutils curl apache2-utils traceroute

COPY sleep.sh /root/sleep.sh
COPY start.sh /root/start.sh

CMD /root/start.sh && /root/sleep.sh
