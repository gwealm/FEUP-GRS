FROM nginx
RUN apt update && apt install -y vim iproute2 iputils-ping tcpdump iptables dnsutils curl apache2-utils
COPY start.sh /root/start.sh
COPY nginx.conf /etc/nginx/conf.d/default.conf
ENTRYPOINT []
CMD /root/start.sh

