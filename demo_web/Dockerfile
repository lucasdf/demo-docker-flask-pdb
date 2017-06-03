FROM python:3.6.1-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY demo_web/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

