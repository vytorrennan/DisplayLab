from django.db import models

# Create your models here.


class carouselItem(models.Model):
    imagem = models.CharField(max_length=512, unique=True, default="")
    url = models.CharField(max_length=512, unique=True, default="")

    def __str__(self):
        return self.url


class membroCategoria(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=200, unique=True, default="")

    def __str__(self):
        return self.categoria


class Membro(models.Model):
    id = models.AutoField(primary_key=True)
    oculto = models.BooleanField(default=False)
    nome = models.CharField(max_length=200, default="")
    categoria = models.ForeignKey(membroCategoria, to_field='categoria', on_delete=models.PROTECT)
    saibaMais = models.CharField(max_length=512, default="")
    foto = models.CharField(max_length=512, default="")
    descricao  = models.CharField(max_length=200, default="")


    def __str__(self):
        return self.nome
