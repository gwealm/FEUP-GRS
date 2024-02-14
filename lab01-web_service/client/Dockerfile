FROM ubuntu:20.04

RUN apt update && apt install -y vim \
iproute2 iputils-ping tcpdump \
iptables dnutils curl

RUN /sbin/ip route replace default via 10.0.1.254

COPY sleep.sh /root/sleep.sh
COPY start.sh /root/start.sh

CMD /root/start.sh && /root/sleep.sh

