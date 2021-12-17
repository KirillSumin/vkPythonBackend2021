FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y libpq-dev python3-dev python3-pip

RUN mkdir /app
WORKDIR /app/

COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY ./libcurl4_7.79.deb /app/
COPY ./curl_7.79.deb /app/
RUN apt-get install -y ./libcurl4_7.79.deb ./curl_7.79.deb


COPY ./browserBasedEcosystem/ /app/
COPY ./wait_and_start_after.sh /app/
COPY ./wait_db.sh /app/
ENTRYPOINT ["./wait_and_start_after.sh"]