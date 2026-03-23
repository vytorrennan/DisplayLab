from coletar_noticias.models import NoticiaExterna
from .scraper import raspar_SBC, raspar_criticalhits
from django.utils import timezone
from datetime import datetime

def salvar_noticias_no_banco(noticias):
    salvas = 0
    duplicadas = 0
    erros = 0
    atualizadas = 0

    for noticia in noticias:
        try:
            titulo = noticia['titulo']
            descricao = noticia['descricao']
            url_fonte = noticia['url_fonte']
            fonte = noticia['fonte']
            data_pub = noticia['data_publicacao']

            # Ignorar URLs inválidas
            if not url_fonte or url_fonte in ('N/A', ''):
                print("URL FONTE VAZIA:", noticia)
                continue

            # Converter data para timezone-aware
            if isinstance(data_pub, datetime) and timezone.is_naive(data_pub):
                data_pub = timezone.make_aware(data_pub)

            # Normalizar imagem
            url_imagem = noticia.get('url_imagem')
            if not url_imagem or url_imagem in ('N/A', ''):
                url_imagem = None

            # SALVA OU ATUALIZA A NOTÍCIA
            obj, created = NoticiaExterna.objects.update_or_create(
                url_fonte=url_fonte,
                defaults={
                    'titulo': titulo,
                    'descricao': descricao,
                    'url_imagem': url_imagem,
                    'fonte': fonte,
                    'data_publicacao': data_pub,
                }
            )

            if created:
                salvas += 1
            else:
                duplicadas += 1
                # só conta como atualizada se o conteúdo mudou
                atualizadas += 1

        except Exception as e:
            erros += 1
            print(f"Erro ao salvar notícia ({noticia.get('url_fonte', 'URL desconhecida')}): {e}")

    return salvas, duplicadas, erros, atualizadas



def coletar_e_salvar_todas():
    estatisticas = {
        'SBC': {'salvas': 0, 'duplicadas': 0, 'erros': 0, 'atualizadas': 0},
        'CRITICAL_HITS': {'salvas': 0, 'duplicadas': 0, 'erros': 0, 'atualizadas': 0},
    }
    
    # Coleta e salva notícias da SBC
    try:
        noticias_sbc = raspar_SBC()
        salvas, duplicadas, erros, atualizadas = salvar_noticias_no_banco(noticias_sbc)
        estatisticas['SBC'] = {'salvas': salvas, 'duplicadas': duplicadas, 'erros': erros, 'atualizadas': atualizadas}
        print(f"SBC: {salvas} salvas, {duplicadas} duplicadas, {atualizadas} atualizadas, {erros} erros")
    except Exception as e:
        print(f"Erro ao coletar notícias da SBC: {e}")
        estatisticas['SBC']['erros'] = 1
    
    # Coleta e salva notícias da Critical Hits
    try:
        noticias_critical = raspar_criticalhits()
        salvas, duplicadas, erros, atualizadas = salvar_noticias_no_banco(noticias_critical)
        estatisticas['CRITICAL_HITS'] = {'salvas': salvas, 'duplicadas': duplicadas, 'erros': erros, 'atualizadas': atualizadas}
        print(f"CRITICAL_HITS: {salvas} salvas, {duplicadas} duplicadas, {atualizadas} atualizadas, {erros} erros")
    except Exception as e:
        print(f"Erro ao coletar notícias da Critical Hits: {e}")
        estatisticas['CRITICAL_HITS']['erros'] = 1
    
    return estatisticas

