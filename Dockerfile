FROM python:3

WORKDIR /usr/src
ADD api /usr/src/api/
ADD requirements.txt /usr/src/
RUN pip install -r requirements.txt

WORKDIR /usr/src/api
