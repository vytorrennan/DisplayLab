from django.db import models
from django.utils.text import slugify
from datetime import datetime

# Create your models here.


class edicao(models.Model):
    id = models.AutoField(primary_key=True)
    edicao = models.PositiveIntegerField(default=0, unique=True)
    
    def __str__(self):
        return str(self.edicao)


class Revista(models.Model):
    id = models.AutoField(primary_key=True)
    oculto = models.BooleanField(default=False)
    gosteis = models.PositiveIntegerField(default=0)
    edicao = models.ForeignKey(edicao, to_field='edicao', on_delete=models.PROTECT)
    dataHora = models.DateTimeField(default=datetime.now)
    url = models.SlugField(max_length=250, unique=True, default="")
    titulo = models.CharField(max_length=250, unique=True, default="")
    autor = models.CharField(max_length=250, default="")
    capa = models.CharField(max_length=512, default="")
    resumo  = models.CharField(max_length=1000, default="")
    pagina = models.TextField(default="")

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super().save(*args, **kwargs)
