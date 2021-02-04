FROM python:3.8.5-alpine

WORKDIR /usr/src/pdf_generator

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
RUN apk add zlib-dev jpeg-dev
RUN apk add xvfb
RUN apk add wkhtmltopdf

RUN mkdir /tmp/runtime-root
RUN chmod 7700 /tmp/runtime-root

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
