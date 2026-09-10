from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from DisplayLab.cron import wrapper_coletar_noticias
from coletar_noticias.models import NoticiaExterna
from coletar_noticias.service.salvar_noticias import coletar_e_salvar_todas
from coletar_noticias.service.scraper import raspar_criticalhits


class NoticiasPageTests(TestCase):
    def test_news_page_renders(self):
        response = self.client.get(reverse("ListaNoticias"))

        self.assertEqual(response.status_code, 200)


class NewsRefreshTests(TestCase):
    def setUp(self):
        self.existing_news = NoticiaExterna.objects.create(
            titulo="Notícia existente",
            descricao="Conteúdo que deve ser preservado.",
            url_fonte="https://example.com/existing",
            fonte="SBC",
            data_publicacao=timezone.now(),
        )

    @patch("DisplayLab.cron.call_command", side_effect=RuntimeError("source unavailable"))
    def test_cron_preserves_existing_news_when_collection_fails(self, _call_command):
        wrapper_coletar_noticias()

        self.assertTrue(
            NoticiaExterna.objects.filter(pk=self.existing_news.pk).exists()
        )

    @patch("coletar_noticias.service.salvar_noticias.raspar_criticalhits", return_value=[])
    @patch("coletar_noticias.service.salvar_noticias.raspar_SBC", return_value=[])
    def test_empty_scrape_preserves_existing_news(self, _raspar_sbc, _raspar_criticalhits):
        estatisticas = coletar_e_salvar_todas()

        self.assertTrue(
            NoticiaExterna.objects.filter(pk=self.existing_news.pk).exists()
        )
        self.assertEqual(estatisticas["SBC"]["erros"], 1)

    @patch("coletar_noticias.service.salvar_noticias.raspar_criticalhits", return_value=[])
    @patch("coletar_noticias.service.salvar_noticias.raspar_SBC")
    def test_successful_scrape_replaces_only_its_source(
        self,
        raspar_sbc,
        _raspar_criticalhits,
    ):
        raspar_sbc.return_value = [{
            "titulo": "Notícia nova",
            "descricao": "Conteúdo atualizado.",
            "url_fonte": "https://example.com/new",
            "url_imagem": None,
            "fonte": "SBC",
            "data_publicacao": timezone.now(),
        }]

        coletar_e_salvar_todas()

        self.assertFalse(
            NoticiaExterna.objects.filter(pk=self.existing_news.pk).exists()
        )
        self.assertTrue(
            NoticiaExterna.objects.filter(url_fonte="https://example.com/new").exists()
        )


class ScraperTests(TestCase):
    @patch("coletar_noticias.service.scraper.requests.get")
    def test_critical_hits_request_has_a_timeout(self, get):
        get.return_value.content = b""

        raspar_criticalhits()

        get.assert_called_once_with(
            "https://criticalhits.com.br/category/games/",
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/91.0.4472.124 Safari/537.36"
                )
            },
            timeout=10,
        )
