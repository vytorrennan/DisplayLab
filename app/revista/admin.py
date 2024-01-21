from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Revista)
admin.site.register(models.edicao)
admin.site.register(models.revistaImagem)
admin.site.register(models.revistaColecaoDeImagem)