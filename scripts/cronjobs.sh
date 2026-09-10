#!/usr/bin/env bash

echo "Aguardando o serviço de banco de dados (pgdb:5432)..."
bash scripts/wait-for-it.sh pgdb:5432 -t 30

echo "Criando diretório do cron..."
mkdir -p /etc/cron.d
touch /etc/cron.d/django_cron
chmod 0644 /etc/cron.d/django_cron

echo "Configurando cron job..."
cd app
python manage.py crontab remove
python manage.py crontab add

echo "Iniciando cron..."
crond -l 2 -f