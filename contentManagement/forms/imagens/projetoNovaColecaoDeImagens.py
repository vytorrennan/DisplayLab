from django import forms
from projetos.models import colecaoDeImagem


class projetoNovaColecaoDeImagensForm(forms.ModelForm):
    class Meta:
        model = colecaoDeImagem
        fields = ["colecao"]