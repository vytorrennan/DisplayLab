from django import forms
from django.contrib import admin
from urllib.parse import urlparse
from . import models

class DisplayCastAdminForm(forms.ModelForm):
    class Meta:
        model = models.DisplayCast
        fields = '__all__'

    def clean_url_youtube(self):
        url = self.cleaned_data.get('url_youtube', '').strip()
        if url and not urlparse(url).scheme:
            url = 'https://' + url
        return url


@admin.register(models.DisplayCast)
class DisplayCastAdmin(admin.ModelAdmin):
    form = DisplayCastAdminForm
    list_display = ['titulo', 'dataHora', 'convidado']
    list_filter = ['dataHora']
    search_fields = ['titulo', 'convidado', 'apresentadores', 'roteirista']
    readonly_fields = ['url']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'url')
        }),
        ('Conteúdo', {
            'fields': ('conteudo', 'capa')
        }),
        ('Vídeo', {
            'fields': ('url_youtube',),
            'description': 'Cole a URL do YouTube (exemplos aceitos: youtube.com/watch?v=VIDEO_ID ou youtu.be/VIDEO_ID)'
        }),
        ('Equipe', {
            'fields': ('convidado', 'apresentadores', 'roteirista')
        }),
        ('Publicação', {
            'fields': ('dataHora',)
        }),
    )
