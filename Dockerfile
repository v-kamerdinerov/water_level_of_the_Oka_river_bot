FROM python:3.10.4-slim-buster
MAINTAINER 'vlad.kamerdinerov@yandex.ru'

ENV TZ="Europe/Moscow"


COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt \
    && rm -rf /tmp/*

COPY app app

ENTRYPOINT ["python3", "-u", "app/main.py"]