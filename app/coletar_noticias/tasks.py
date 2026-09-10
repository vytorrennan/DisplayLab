"""
Tarefas para coletar e salvar notícias no banco de dados.
Pode ser usado com django-crontab ou chamado manualmente.
"""
from coletar_noticias.service.salvar_noticias import coletar_e_salvar_todas


def coletar_noticias():
    """
    Função para ser chamada pelo cron ou manualmente.
    Coleta notícias de todas as fontes e salva no banco.
    """
    estatisticas = coletar_e_salvar_todas()
    return estatisticas