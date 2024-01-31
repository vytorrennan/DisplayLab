from django.db import models
from django.utils.text import slugify
from datetime import datetime

# Create your models here.


class Projeto(models.Model):
    id = models.AutoField(primary_key=True)
    oculto = models.BooleanField(default=False)
    gosteis = models.PositiveIntegerField(default=0)
    dataHora = models.DateTimeField(default=datetime.now)
    url = models.SlugField(max_length=250, unique=True, default="")
    titulo = models.CharField(max_length=250, unique=True, default="")
    capa = models.CharField(max_length=512, default="")
    resumo = models.CharField(max_length=1000, default="")
    pagina = models.TextField(default="")

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super().save(*args, **kwargs)


class projetoColecaoDeImagem(models.Model):
    id = models.AutoField(primary_key=True)
    colecao = models.SlugField(max_length=250, unique=True, default="")

    def __str__(self):
        return self.colecao


def image_upload_path(instance, filename):
    return "./projetos/media/uploadsProjetos/" + instance.colecao.colecao + "/" + filename


class projetoImagem(models.Model):
    id = models.AutoField(primary_key=True)
    colecao = models.ForeignKey(
        projetoColecaoDeImagem, to_field="colecao", on_delete=models.PROTECT
    )
    imagem = models.ImageField(upload_to=image_upload_path)

    def __str__(self):
        return self.imagem.name.replace("projetos/static/uploads/", "")
