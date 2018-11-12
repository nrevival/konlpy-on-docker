FROM ubuntu:16.04
MAINTAINER Jonghyuck Park <nrevival@gmail.com>

RUN apt-get update
RUN apt-get install -y g++ openjdk-8-jdk python3 python3-dev python3-pip curl
RUN pip3 install konlpy bottle gunicorn

RUN bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)

EXPOSE 8899