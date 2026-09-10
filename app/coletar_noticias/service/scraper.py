import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin


def normalizar_url_imagem(url_imagem, url_base):
    """
    Normaliza a URL da imagem, convertendo URLs relativas para absolutas.
    """
    if not url_imagem or url_imagem in ('N/A', '', None):
        return None

    # Se já é uma URL absoluta, retorna como está
    if url_imagem.startswith('http://') or url_imagem.startswith('https://'):
        return url_imagem

    # Se é uma URL relativa, converte para absoluta
    if url_imagem.startswith('//'):
        return 'https:' + url_imagem

    # Converte URL relativa para absoluta usando urljoin
    return urljoin(url_base, url_imagem)


def extrair_url_imagem(img_tag, url_base):
    """
    Extrai a URL da imagem de uma tag img, tentando múltiplos atributos.
    """
    if not img_tag:
        return None

    # Tenta diferentes atributos na ordem de prioridade
    atributos = ['data-src', 'data-img-url', 'src', 'data-lazy-src', 'data-original']

    for attr in atributos:
        url = img_tag.get(attr)
        if url:
            # Se for srcset, pega a primeira URL
            if attr == 'src' and 'srcset' in img_tag.attrs:
                srcset = img_tag.get('srcset', '')
                if srcset:
                    # srcset pode ter múltiplas URLs separadas por vírgula
                    primeira_url = srcset.split(',')[0].strip().split(' ')[0]
                    if primeira_url:
                        return normalizar_url_imagem(primeira_url, url_base)

            # Remove query strings e fragmentos desnecessários
            if url:
                return normalizar_url_imagem(url, url_base)

    # Tenta extrair do srcset diretamente
    srcset = img_tag.get('srcset', '')
    if srcset:
        primeira_url = srcset.split(',')[0].strip().split(' ')[0]
        if primeira_url:
            return normalizar_url_imagem(primeira_url, url_base)

    return None


def raspar_SBC():
    url = "https://www.sbc.org.br/noticias/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição HTTP para SBC: {e}")
        return []

    noticias = []

    artigos = soup.find_all('div', class_=lambda c: c and 'wp-block-kubio-query-loop-item' in c)

    for artigo in artigos[:10]:  # Limitar a 10 notícias
        titulo = 'Título não encontrado'
        url_fonte = 'N/A'

        try:
            # titulo e link
            link_tag = artigo.select_one('.wp-block-kubio-post-title__link')
            titulo_tag = link_tag.find('h4') if link_tag else None

            # titulo e url
            titulo = titulo_tag.get_text(strip=True) if titulo_tag else titulo
            url_fonte = link_tag['href'] if link_tag and link_tag.get('href') else url_fonte

            # descrição
            descricao_tag = artigo.select_one('.wp-block-kubio-post-excerpt__text')
            descricao = descricao_tag.get_text(strip=True) if descricao_tag else titulo

            # imagem - tenta múltiplos seletores
            img_tag = None
            seletores_imagem = [
                '.wp-block-kubio-post-featured-image__image',
                '.wp-block-kubio-post-featured-image img',
                'img.wp-block-kubio-post-featured-image__image',
                'img'
            ]

            for seletor in seletores_imagem:
                img_tag = artigo.select_one(seletor)
                if img_tag:
                    break

            url_imagem = extrair_url_imagem(img_tag, url) if img_tag else None

            # data
            data_publicacao = datetime.now()

            # fonte
            fonte_escolhida = "SBC"

            noticias.append({
                'titulo': titulo,
                'descricao': descricao,
                'url_fonte': url_fonte,
                'url_imagem': url_imagem,
                'fonte': fonte_escolhida,
                'data_publicacao': data_publicacao,
            })

        except Exception as e:
            print(f"Erro ao processar um artigo ({url_fonte}): {e}")
            continue

    return noticias


def raspar_criticalhits():
    url = "https://criticalhits.com.br/category/games/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    noticias = []

    artigos = soup.find_all('div', class_='tdb_module_loop')

    for artigo in artigos:
        try:
            # titulo e link
            link_tag = artigo.select_one('h3.entry-title a')

            # titulo e url
            titulo = link_tag.get_text(strip=True) if link_tag else 'Título não encontrado'
            url_fonte = link_tag['href'] if link_tag and link_tag.get('href') else 'N/A'

            # imagem - tenta múltiplos seletores
            img_tag = None
            seletores_imagem = [
                '.entry-thumb',
                '.entry-thumb img',
                'img.entry-thumb',
                '.td-module-thumb img',
                'img'
            ]

            for seletor in seletores_imagem:
                img_tag = artigo.select_one(seletor)
                if img_tag:
                    break

            if not img_tag:
                img_tag = artigo.find('img')

            url_imagem = extrair_url_imagem(img_tag, url) if img_tag else None

            # descrição
            descricao = titulo

            # data
            data_tag = artigo.select_one('time.td-module-date')
            if data_tag and data_tag.get('datetime'):
                data_publicacao_str = data_tag.get('datetime').split('T')[0]
                data_publicacao = datetime.strptime(data_publicacao_str, '%Y-%m-%d')
            else:
                data_publicacao = datetime.now()

            fonte_escolhida = "CRITICAL_HITS"

            noticias.append({
                'titulo': titulo,
                'descricao': descricao,
                'url_fonte': url_fonte,
                'url_imagem': url_imagem,
                'fonte': fonte_escolhida,
                'data_publicacao': data_publicacao,
            })

        except Exception as e:
            url_fonte_erro = url_fonte if 'url_fonte' in locals() else 'URL desconhecida'
            print(f"Erro ao processar um artigo: {e}. URL: {url_fonte_erro}")
            continue

    return noticias
