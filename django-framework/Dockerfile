# syntax=docker/dockerfile:1
FROM python:3.10
WORKDIR /code
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
