FROM nginx
RUN apt update && apt install -y vim iproute2 iputils-ping tcpdump iptables dnsutils curl apache2-utils 
COPY start.sh /root/start.sh

EXPOSE 80

COPY ./static/ /usr/share/nginx/html

ENTRYPOINT []
CMD /root/start.sh
