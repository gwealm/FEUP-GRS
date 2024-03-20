FROM ubuntu/squid:latest

RUN apt update && apt install -y vim iproute2 iputils-ping

COPY ectsquid/squid.conf etc/squid/squid.conf

COPY start.sh /root/start.sh

# ENTRYPOINT [ ]
# CMD /root/start.sh