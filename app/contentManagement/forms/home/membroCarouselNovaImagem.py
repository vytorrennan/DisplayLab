from django import forms
from main.models import membroCarouselImagem


class membroCarouselNovaImagemForm(forms.ModelForm):
    class Meta:
        model = membroCarouselImagem
        fields = ["colecao", "imagem"]
