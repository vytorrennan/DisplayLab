from django import forms
from revista.models import revistaColecaoDeImagem


class revistaNovaColecaoDeImagensForm(forms.ModelForm):
    class Meta:
        model = revistaColecaoDeImagem
        fields = ["colecao"]