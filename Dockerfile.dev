FROM python:3.8-alpine
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev bash libffi-dev make
WORKDIR /usr/src/app
COPY requirements.txt .
COPY dev-requirements.txt .
RUN pip install -r dev-requirements.txt
COPY . .
