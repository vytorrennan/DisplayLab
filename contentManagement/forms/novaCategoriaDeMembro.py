from django import forms
from main.models import Categoria


class novaCategoriaDeMembroForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["categoria"]