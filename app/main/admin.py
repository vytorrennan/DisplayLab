from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.carouselItem)
admin.site.register(models.Membro)
admin.site.register(models.membroCategoria)
admin.site.register(models.membroCarouselColecaoDeImagem)
admin.site.register(models.membroCarouselImagem)