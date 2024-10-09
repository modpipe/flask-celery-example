FROM python:3.12

RUN groupadd -g 1000 python && useradd -s "/usr/bin/env bash" --create-home -d /flask --no-log-init -u 1000 -g 1000 python && chown 1000:1000 /flask

WORKDIR /flask

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chown -R 1000:1000 /flask

USER 1000:1000