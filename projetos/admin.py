from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Projeto)
admin.site.register(models.projetoImagem)
admin.site.register(models.colecaoDeImagem)