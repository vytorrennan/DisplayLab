FROM python:3.12.1-alpine3.19

RUN apk add --no-cache \
    postgresql-client \
    postgresql-dev \
    pkgconfig \
    git \
    gcc \
    libcurl \
    python3-dev \
    gpgme-dev \
    libc-dev

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt --no-cache-dir --disable-pip-version-check

COPY ./ ./

EXPOSE 8000