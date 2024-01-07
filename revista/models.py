from django.db import models

# Create your models here.


class Revista(models.Model):
    id = models.AutoField(primary_key=True),
    deletado = models.BooleanField(),
    gosteis = models.PositiveIntegerField(),
    url = models.CharField(max_length=512, unique=True),
    titulo = models.CharField(max_length=512, unique=True),
    capa = models.CharField(max_length=512),
    resumo  = models.CharField(max_length=2048),
    pagina = models.TextField(),
