from django import forms
from revista.models import Revista
from tinymce.widgets import TinyMCE


class novoPostRevistaForm(forms.ModelForm):
    class Meta:
        model = Revista
        fields = ["titulo", "edicao", "autor", "capa", "resumo", "pagina"]
        widgets = {
            'pagina': TinyMCE()
        }