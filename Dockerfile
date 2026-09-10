FROM python:3.12.1-alpine3.19

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    bash \
    postgresql-client \
    postgresql-dev \
    gcc \
    musl-dev \
    python3-dev \
    libc-dev \
    git \
    pkgconfig \
    libcurl \
    gpgme-dev \
    dcron \
    netcat-openbsd

WORKDIR /DisplayLab

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Garantir que scripts são executáveis
RUN chmod +x scripts/displaylab.sh \
    && chmod +x scripts/wait-for-it.sh \
    && chmod +x scripts/cronjobs.sh

# Criar log do cron
RUN mkdir -p /var/log \
    && touch /var/log/cron.log \
    && chmod 777 /var/log/cron.log

# Wrapper neutro
RUN printf '#!/bin/sh\nexec "$@"\n' > /entrypoint.sh \
    && chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
