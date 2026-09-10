from pathlib import Path

from django.conf import settings
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.utils import timezone

from displaycast.models import DisplayCast


class PublicNavigationTests(TestCase):
    def test_home_game_cards_link_to_project_detail_routes(self):
        response = self.client.get(reverse("home"))

        self.assertContains(response, 'href="/projetos/peruacu-digital/"', count=2)
        self.assertContains(response, 'href="/projetos/indisciplina-2d/"', count=2)
        self.assertContains(response, 'href="/projetos/exterminando-drogas/"', count=2)

    def test_search_returns_matching_content(self):
        displaycast = DisplayCast.objects.create(
            titulo="Tecnologia assistiva",
            conteudo="Um episódio sobre acessibilidade digital.",
            dataHora=timezone.now(),
        )

        response = self.client.get(reverse("busca"), {"q": "assistiva"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, displaycast.titulo)
        self.assertContains(response, reverse("displaycast_detail", args=[displaycast.url]))


class DeploymentEntrypointTests(SimpleTestCase):
    def test_web_entrypoint_uses_gunicorn_without_collecting_news(self):
        script_path = Path(settings.BASE_DIR).parent / "scripts" / "displaylab.sh"
        script = script_path.read_text()

        self.assertIn("gunicorn DisplayLab.wsgi:application", script)
        self.assertNotIn("python manage.py runserver", script)
        self.assertNotIn("python manage.py coletar_noticias", script)

    def test_restore_is_validated_before_the_current_database_is_replaced(self):
        script_path = Path(settings.BASE_DIR).parent / "scripts" / "restore-backup.sh"
        script = script_path.read_text()

        self.assertNotIn("DROP SCHEMA public CASCADE", script)
        self.assertIn('POSTGRES_DB="${restore_database}"', script)
        self.assertLess(
            script.index('POSTGRES_DB="${restore_database}"'),
            script.index('ALTER DATABASE :"restore_database" RENAME TO :"target_database"'),
        )
