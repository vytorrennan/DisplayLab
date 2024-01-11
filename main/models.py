from django.db import models

# Create your models here.


class carouselItem(models.Model):
    imagem = models.CharField(max_length=512, unique=True, default="")
    url = models.CharField(max_length=512, unique=True, default="")


class Membro(models.Model):
    id = models.AutoField(primary_key=True)
    deletado = models.BooleanField(default=False)
    nome = models.CharField(max_length=200, default="")
    categoria = models.CharField(max_length=200, default="")
    saibaMais = models.CharField(max_length=512, default="")
    foto = models.CharField(max_length=512, default="")
    descricao  = models.CharField(max_length=200, default="")


    def __str__(self):
        return self.nome
