from django import forms
from main.models import membroCategoria


class novaCategoriaDeMembroForm(forms.ModelForm):
    class Meta:
        model = membroCategoria
        fields = ["categoria"]