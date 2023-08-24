FROM python:3.10

RUN mkdir /test

WORKDIR /test

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
