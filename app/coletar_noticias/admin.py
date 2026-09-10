from django.contrib import admin
from .models import NoticiaExterna


@admin.register(NoticiaExterna)
class NoticiaExternaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fonte', 'data_publicacao', 'url_fonte', 'url_imagem', 'descricao')
    list_filter = ('fonte', 'data_publicacao')
    search_fields = ('titulo', 'descricao', 'fonte')
    readonly_fields = ('url_fonte', 'url_imagem', 'data_publicacao')
    ordering = ('-data_publicacao',)

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'fonte')
        }),
        ('URLs', {
            'fields': ('url_fonte', 'url_imagem')
        }),
        ('Data', {
            'fields': ('data_publicacao',)
        }),
    )