from django.db import models

# Create your models here.


class ItensDoCarousel(models.Model):
    imagem = models.CharField(max_length=512, unique=True),
    url = models.CharField(max_length=512, unique=True),


class Membros(models.Model):
    id = models.AutoField(primary_key=True),
    deletado = models.BooleanField(),
    nome = models.CharField(max_length=200),
    categoria = models.CharField(max_length=200),
    linkedin = models.CharField(max_length=512),
    descricao  = models.CharField(max_length=200),
