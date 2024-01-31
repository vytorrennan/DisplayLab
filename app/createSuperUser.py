#!/usr/bin/env python
import environ
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DisplayLab.settings")
django.setup()
env = environ.Env()
environ.Env.read_env()
from django.contrib.auth.models import User

if User.objects.filter(username=env("DJANGO_SUPERUSER_USERNAME")).first() is None:
    User.objects.create_superuser(
        env("DJANGO_SUPERUSER_USERNAME"),
        env("DJANGO_SUPERUSER_EMAIL"),
        env("DJANGO_SUPERUSER_PASSWORD"),
    )
    print("Nenhum user com o username do arquivo .env foi encontrado, logo ele foi criado")
