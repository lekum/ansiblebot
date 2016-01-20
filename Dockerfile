FROM ubuntu:14.04
MAINTAINER Alejandro Guirao <lekumberri@gmail.com>
ENV REFRESHED_AT 2016-01-20

RUN mkdir -p /opt/bot
WORKDIR /opt/bot
RUN mkdir -p data
RUN apt-get update && apt-get install -y -qq python-virtualenv python-dev libffi-dev libssl-dev
RUN virtualenv venv
COPY src /opt/bot
RUN venv/bin/pip install -r requirements.txt
CMD ["venv/bin/errbot"]
