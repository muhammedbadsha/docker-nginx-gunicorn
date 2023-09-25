FROM python:3.8

ENV PYTHONUNBOFFERED 1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


