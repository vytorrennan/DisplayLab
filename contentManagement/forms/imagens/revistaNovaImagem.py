from django import forms
from revista.models import revistaImagem


class revistaNovaImagemForm(forms.ModelForm):
    class Meta:
        model = revistaImagem
        fields = ["colecao", "imagem"]