FROM ubuntu:18.04


RUN apt-get upgrade
RUN apt-get update
RUN apt-get -y install python3-pip
RUN mkdir /src
WORKDIR /src
COPY ./src/requirements.txt /scripts/
RUN pip3 install -r /scripts/requirements.txt
