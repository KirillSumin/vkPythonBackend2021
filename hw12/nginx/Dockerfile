FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y nginx

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./static/ /www/static/

ENTRYPOINT ["nginx", "-g", "daemon off;"]
