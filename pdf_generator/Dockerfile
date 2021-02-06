FROM python:3.8.5-alpine
FROM ubuntu:20.04

WORKDIR /usr/src/pdf_generator

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND="noninteractive"

RUN apt-get update 
RUN apt-get install -y gcc python3-dev python3-pip musl-dev libffi-dev libpq-dev
RUN apt-get install -y xvfb libfontconfig wkhtmltopdf

COPY ./requirements.txt .
 
RUN pip3 install -r requirements.txt

COPY . .
