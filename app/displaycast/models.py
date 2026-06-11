from django.db import models
from django.utils.text import slugify
from datetime import datetime
from urllib.parse import urlparse, parse_qs
import re

class DisplayCast(models.Model):
    titulo = models.CharField(max_length=250, unique=True, default="")
    dataHora = models.DateTimeField(default=datetime.now)
    conteudo = models.TextField(blank=True, default="")
    capa = models.CharField(max_length=512, blank=True, default="")
    url_youtube = models.URLField(max_length=512, blank=True, default="")
    convidado = models.CharField(max_length=250, blank=True, default="")
    apresentadores = models.CharField(max_length=250, blank=True, default="")
    roteirista = models.CharField(max_length=250, blank=True, default="")
    url = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        ordering = ['-dataHora']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.titulo)

        if self.url_youtube:
            youtube_url = self.url_youtube.strip()
            if youtube_url and not urlparse(youtube_url).scheme:
                youtube_url = 'https://' + youtube_url
            self.url_youtube = youtube_url

        super().save(*args, **kwargs)

    def _normalize_youtube_id(self, candidate: str) -> str | None:
        candidate = candidate.strip()
        if len(candidate) == 11 and re.match(r'^[0-9A-Za-z_-]{11}$', candidate):
            return candidate
        return None

    def get_youtube_embed_id(self):
        """
        Extrai o ID do YouTube da URL e retorna a URL de embed.
        Suporta várias formas de URL e parâmetros adicionais.
        """
        url = (self.url_youtube or '').strip()
        if not url:
            return None

        if not urlparse(url).scheme:
            url = 'https://' + url

        parsed = urlparse(url)
        hostname = (parsed.hostname or '').lower()
        path = parsed.path or ''

        if hostname.endswith('youtu.be'):
            candidate = path.lstrip('/').split('/')[0]
            return self._normalize_youtube_id(candidate)

        if 'youtube.com' in hostname or 'youtube-nocookie.com' in hostname:
            if path.startswith('/watch'):
                query = parse_qs(parsed.query)
                video_id = query.get('v', [''])[0]
                normalized = self._normalize_youtube_id(video_id)
                if normalized:
                    return normalized
            for segment in ('/embed/', '/shorts/', '/v/'):
                if path.startswith(segment):
                    candidate = path.split('/')[2] if len(path.split('/')) >= 3 else ''
                    normalized = self._normalize_youtube_id(candidate)
                    if normalized:
                        return normalized

        # Fallback - pegar ID de url não padrão
        match = re.search(r'(?:youtube\.com\/(?:watch\?v=|watch\?.+&v=|embed\/|shorts\/|v\/)|youtu\.be\/)([0-9A-Za-z_-]{11})', url)
        if match:
            return match.group(1)

        return None

    def get_embed_url(self):
        """Retorna a URL pronta para embed no iframe"""
        video_id = self.get_youtube_embed_id()
        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return None

    @property
    def embed_url(self):
        return self.get_embed_url()
