from django.db import models
from django.utils import timezone

class NoticiaExterna(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    url_fonte = models.URLField(unique=True)
    url_imagem = models.TextField(blank=True, null=True)

    fonte = models.CharField(max_length=255)

    data_publicacao = models.DateTimeField()

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo