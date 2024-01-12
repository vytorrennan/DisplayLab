from django import forms
from revista.models import Revista
from tinymce.widgets import TinyMCE


class novoPostRevistaForm(forms.ModelForm):
    class Meta:
        model = Revista
        fields = ["oculto", "titulo", "edicao", "dataHora", "autor", "capa", "resumo", "pagina"]
        widgets = {
            'dataHora': forms.DateTimeInput(),
            'pagina': TinyMCE()
        }