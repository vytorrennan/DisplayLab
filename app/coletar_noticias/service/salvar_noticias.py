from datetime import datetime

from django.db import transaction
from django.utils import timezone

from coletar_noticias.models import NoticiaExterna

from .scraper import raspar_SBC, raspar_criticalhits


def salvar_noticias_no_banco(noticias, fonte_esperada=None):
    salvas = 0
    duplicadas = 0
    erros = 0
    atualizadas = 0
    urls_coletadas = []

    with transaction.atomic():
        for noticia in noticias:
            try:
                titulo = noticia['titulo']
                descricao = noticia['descricao']
                url_fonte = noticia['url_fonte']
                fonte = noticia['fonte']
                data_pub = noticia['data_publicacao']

                if fonte_esperada and fonte != fonte_esperada:
                    raise ValueError(
                        f"Fonte inesperada: {fonte}. Esperada: {fonte_esperada}."
                    )

                if not url_fonte or url_fonte in ('N/A', ''):
                    raise ValueError("URL da fonte vazia")

                if isinstance(data_pub, datetime) and timezone.is_naive(data_pub):
                    data_pub = timezone.make_aware(data_pub)

                url_imagem = noticia.get('url_imagem')
                if not url_imagem or url_imagem in ('N/A', ''):
                    url_imagem = None

                defaults = {
                    'titulo': titulo,
                    'descricao': descricao,
                    'url_imagem': url_imagem,
                    'fonte': fonte,
                    'data_publicacao': data_pub,
                }
                existente = NoticiaExterna.objects.filter(
                    url_fonte=url_fonte
                ).first()
                mudou = existente is not None and any(
                    getattr(existente, campo) != valor
                    for campo, valor in defaults.items()
                )

                _, created = NoticiaExterna.objects.update_or_create(
                    url_fonte=url_fonte,
                    defaults=defaults,
                )
                urls_coletadas.append(url_fonte)

                if created:
                    salvas += 1
                else:
                    duplicadas += 1
                    if mudou:
                        atualizadas += 1

            except (KeyError, TypeError, ValueError) as exc:
                erros += 1
                print(
                    "Erro ao validar notícia "
                    f"({noticia.get('url_fonte', 'URL desconhecida')}): {exc}"
                )

        if fonte_esperada and urls_coletadas and erros == 0:
            NoticiaExterna.objects.filter(fonte=fonte_esperada).exclude(
                url_fonte__in=urls_coletadas
            ).delete()

    return salvas, duplicadas, erros, atualizadas


def coletar_e_salvar_todas():
    fontes = {
        'SBC': raspar_SBC,
        'CRITICAL_HITS': raspar_criticalhits,
    }
    estatisticas = {}

    for fonte, coletor in fontes.items():
        try:
            noticias = coletor()
            if not noticias:
                raise ValueError("A fonte não retornou notícias")

            salvas, duplicadas, erros, atualizadas = salvar_noticias_no_banco(
                noticias,
                fonte_esperada=fonte,
            )
            estatisticas[fonte] = {
                'salvas': salvas,
                'duplicadas': duplicadas,
                'erros': erros,
                'atualizadas': atualizadas,
            }
            print(
                f"{fonte}: {salvas} salvas, {duplicadas} duplicadas, "
                f"{atualizadas} atualizadas, {erros} erros"
            )
        except Exception as exc:
            print(f"Erro ao coletar notícias de {fonte}: {exc}")
            estatisticas[fonte] = {
                'salvas': 0,
                'duplicadas': 0,
                'erros': 1,
                'atualizadas': 0,
            }

    return estatisticas
