from django import forms
from revista.models import edicao


class novoOuEditarEdicaoDeRevistaForm(forms.ModelForm):
    class Meta:
        model = edicao
        fields = ["edicao"]