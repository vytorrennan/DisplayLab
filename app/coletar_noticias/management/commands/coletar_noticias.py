from django.core.management.base import BaseCommand
from coletar_noticias.tasks import coletar_e_salvar_todas

class Command(BaseCommand):
    help = "Coleta notícias das fontes e salva no banco"

    def handle(self, *args, **kwargs):
        estatisticas = coletar_e_salvar_todas()
        self.stdout.write(self.style.SUCCESS("Coleta finalizada!"))
        
        for fonte, dados in estatisticas.items():
            self.stdout.write(
                f"{fonte}: {dados['salvas']} salvas, "
                f"{dados['duplicadas']} duplicadas, "
                f"{dados['atualizadas']} atualizadas, "
                f"{dados['erros']} erros"
            )
