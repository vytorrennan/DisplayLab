from django import forms
from alumni.models import Aluno, edicao

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            "nome",
            "descricao",
            "perfilLinkedIn",
            "perfilLattes",
            "foto",
        ]