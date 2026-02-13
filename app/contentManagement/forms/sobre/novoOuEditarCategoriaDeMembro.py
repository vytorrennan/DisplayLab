from django import forms
from main.models import membroCategoria


class novoOuEditarCategoriaDeMembroForm(forms.ModelForm):
    class Meta:
        model = membroCategoria
        fields = ["categoria", "oculto"]