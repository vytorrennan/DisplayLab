from django import forms
from alumni.models import Aluno, edicao

class EdicaoForm(forms.ModelForm):
    class Meta:
        model = edicao
        fields = ["edicao"]