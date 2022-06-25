FROM python:3.8.5-alpine

RUN pip install --upgrade pip

RUN apk add build-base

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]