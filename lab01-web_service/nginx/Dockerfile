FROM nginx
RUN apt update && apt install -y vim iproute2 iputils-ping tcpdump iptables dnsutils curl
COPY start.sh /root/start.sh
ENTRYPOINT []
CMD /root/start.sh
