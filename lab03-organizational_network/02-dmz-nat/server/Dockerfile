FROM nginx
RUN apt update && apt install -y vim iproute2 iputils-ping tcpdump iptables dnsutils curl apache2-utils

EXPOSE 80

COPY ./static/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY sleep.sh /root/sleep.sh