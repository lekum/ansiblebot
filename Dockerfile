FROM python:3
LABEL maintainer Alejandro Guirao <lekumberri@gmail.com>
ENV REFRESHED_AT 2017-06-23
# Set the locale
RUN apt-get update && apt-get install -y -qq libffi-dev libssl-dev openssh-client
WORKDIR /opt/bot/
RUN mkdir -p data
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src .
CMD ["errbot"]
