FROM ubuntu:20.04
RUN apt update && apt install -y vim iproute2 iputils-ping tcpdump iptables dnsutils curl telnet wget
COPY sleep.sh /root/sleep.sh
RUN chmod +x /root/sleep.sh
CMD /root/sleep.sh