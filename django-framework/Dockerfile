# syntax=docker/dockerfile:1
FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py makemigrations
RUN python manage.py migrate --run-syncdb
RUN python population_script.py