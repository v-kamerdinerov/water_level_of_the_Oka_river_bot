FROM python:3.10.4-alpine
MAINTAINER 'vlad.kamerdinerov@yandex.ru'

ENV TZ="Europe/Moscow"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt \
    && rm -rf requirements.txt

COPY app .

ENTRYPOINT ["python3", "-u", "/app/main.py"]