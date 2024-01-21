from django import forms
from main.models import membroCarouselColecaoDeImagem


class membroCarouselNovaColecaoDeImagensForm(forms.ModelForm):
    class Meta:
        model = membroCarouselColecaoDeImagem
        fields = ["colecao"]