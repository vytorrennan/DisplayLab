from django import forms
from projetos.models import projetoImagem


class projetoNovaImagemForm(forms.ModelForm):
    class Meta:
        model = projetoImagem
        fields = ["colecao", "imagem"]