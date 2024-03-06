FROM ubuntu:20.04

# baseline network tools
RUN apt update && apt install -y vim iproute2 iputils-ping tcpdump iptables dnsutils curl

# quagga
RUN apt update && apt install -y quagga systemctl
RUN apt update && apt install -y telnet

RUN mkdir -p /var/log/quagga

RUN chown quagga:quagga /var/log/quagga

RUN mkdir /run/quagga

RUN chmod a+w /run/quagga

COPY sleep.sh /root/sleep.sh
COPY start.sh /root/start.sh

CMD /root/start.sh