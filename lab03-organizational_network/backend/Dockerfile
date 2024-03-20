FROM nginx
RUN apt update && apt install -y vim iproute2 iputils-ping tcpdump iptables dnsutils curl apache2-utils python3
COPY start.sh /root/start.sh

EXPOSE 80

COPY ./static/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

CMD /root/start.sh