from django.views import View
from django.shortcuts import render
from django.db.models import Q
from . import models
from revista.models import Revista
from projetos.models import Projeto
from coletar_noticias.models import NoticiaExterna
from displaycast.models import DisplayCast


class home(View):
    def get(self, request):
        carousel = models.carouselItem.objects.all()
        numItens = carousel.count()
        ultimosPosts = Revista.objects.filter(oculto=False).order_by("-edicao", "-dataHora")[0:3]
        displaycasts = DisplayCast.objects.order_by('-dataHora')[:3]

        noticias_sbc = NoticiaExterna.objects.filter(fonte='SBC').order_by('-data_publicacao')[0:10]
        noticias_games = NoticiaExterna.objects.filter(fonte='CRITICAL_HITS').order_by('-data_publicacao')[0:10]
        context = {
            "carousel": carousel,
            "iterableNumItens": range(numItens),
            "ultimosPosts": ultimosPosts,
            "displaycasts": displaycasts,
            "noticias_sbc": noticias_sbc,
            "noticias_games": noticias_games
        }


        return render(request, "home.html", context)


class busca(View):
    def get(self, request):
        termo = request.GET.get("q", "").strip()
        context = {
            "termo": termo,
            "projetos": Projeto.objects.none(),
            "revistas": Revista.objects.none(),
            "displaycasts": DisplayCast.objects.none(),
            "noticias": NoticiaExterna.objects.none(),
        }

        if termo:
            context.update({
                "projetos": Projeto.objects.filter(
                    Q(titulo__icontains=termo)
                    | Q(resumo__icontains=termo)
                    | Q(pagina__icontains=termo),
                    oculto=False,
                )[:20],
                "revistas": Revista.objects.filter(
                    Q(titulo__icontains=termo)
                    | Q(resumo__icontains=termo)
                    | Q(pagina__icontains=termo),
                    oculto=False,
                )[:20],
                "displaycasts": DisplayCast.objects.filter(
                    Q(titulo__icontains=termo)
                    | Q(conteudo__icontains=termo)
                    | Q(convidado__icontains=termo)
                    | Q(apresentadores__icontains=termo)
                    | Q(roteirista__icontains=termo)
                )[:20],
                "noticias": NoticiaExterna.objects.filter(
                    Q(titulo__icontains=termo)
                    | Q(descricao__icontains=termo)
                    | Q(fonte__icontains=termo)
                )[:20],
            })

        return render(request, "busca.html", context)

class institucional(View):
    def get(self, request):
        return render(request, "institucional.html")


class sobre(View):
    def get(self, request):
        membros = models.Membro.objects.filter(oculto=False)
        categorias = models.membroCategoria.objects.filter(oculto=False)
        context = {"membros": membros, "categorias": categorias}
        return render(request, "sobre.html", context)

class parceiros(View):
    def get(self, request):
        return render(request, "parceiros.html")

class expediente(View):
    def get(sef, request):
        membros = models.Membro.objects.all().order_by('categoria', 'nome')
        return render(request, "expediente.html",{'membros': membros})

class mapa(View):
    def get(self, request):
        return render(request, "map.html")

class acessibilidade(View):
    def get(self, request):
        return render(request, "acessibilidade.html")

class contato(View):
    def get(self, request):
        return render(request, "contatos.html")
