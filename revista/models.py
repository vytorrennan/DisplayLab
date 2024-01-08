from django.db import models

# Create your models here.


class Revista(models.Model):
    id = models.AutoField(primary_key=True)
    deletado = models.BooleanField(default=False)
    gosteis = models.PositiveIntegerField(default=0)
    url = models.CharField(max_length=250, unique=True, default="")
    titulo = models.CharField(max_length=250, unique=True, default="")
    capa = models.CharField(max_length=512, default="")
    resumo  = models.CharField(max_length=1000, default="")
    pagina = models.TextField(default="")
