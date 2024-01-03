from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projetos", views.projetos, name="projetos"),
    path("institucional", views.institucional, name="institucional"),
    path("sobre", views.sobre, name="sobre"),
    #temporarios-------
    path("projetos/displayCast", views.displayCast, name="displayCast"),
    path("projetos/educaRedes", views.educaRedes, name="educaRedes"),
    path("projetos/exterminandoDrogas", views.exterminandoDrogas, name="exterminandoDrogas"),
    path("projetos/peruacuDigital", views.peruacuDigital, name="peruacuDigital"),
    #------------------
]