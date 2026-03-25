from django.db import models
from django.utils.text import slugify
from datetime import datetime
import os

def aluno_upload_path(instance, filename):
    return os.path.join('alumni', 'uploadsAlunos', instance.nome, filename)

class edicao(models.Model):
    id = models.AutoField(primary_key=True)
    edicao = models.PositiveIntegerField(default=0, unique=True)

    def __str__(self):
        return str(self.edicao)

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250, unique=True, default="")
    descricao = models.CharField(max_length=250, default="")
    funcao = models.CharField(max_length=255, default="")
    perfilLinkedIn = models.URLField(max_length=512, default="")
    perfilLattes = models.URLField(max_length=512, default="")
    foto = models.ImageField(
            upload_to=aluno_upload_path, 
            default='alumni/default.jpg' 
        )
    dataHora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome