from django import forms
from main.models import Membro


class novoMembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ["nome", "descricao", "categoria","oculto", "foto", "saibaMais"]