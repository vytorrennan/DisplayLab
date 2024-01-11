from django import forms
from revista.models import edicao


class novaEdicaoDeRevistaForm(forms.ModelForm):
    class Meta:
        model = edicao
        fields = ["edicao"]