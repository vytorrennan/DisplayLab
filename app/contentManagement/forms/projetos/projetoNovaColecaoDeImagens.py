from django import forms
from projetos.models import projetoColecaoDeImagem


class projetoNovaColecaoDeImagensForm(forms.ModelForm):
    class Meta:
        model = projetoColecaoDeImagem
        fields = ["colecao"]