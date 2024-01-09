from django import forms
from main.models import Membros


class novoMembroForm(forms.ModelForm):
    class Meta:
        model = Membros
        fields = ["nome", "descricao", "categoria", "linkedin"]