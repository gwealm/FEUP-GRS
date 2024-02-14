FROM nginx
RUN apt update && apt install -y vim iproute2 iputils-ping tcmdump iptables dnsutils curl
COPY start.sh /root/start.sh
ENTRYPOINT []
CMD /root/start.sh
