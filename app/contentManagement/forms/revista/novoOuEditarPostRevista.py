from django import forms
from revista.models import Revista
from tinymce.widgets import TinyMCE


class novoOuEditarPostRevistaForm(forms.ModelForm):
    class Meta:
        model = Revista
        fields = ["titulo", "oculto", "edicao", "dataHora", "autor", "capa", "resumo", "pagina"]
        widgets = {
            'dataHora': forms.DateTimeInput(),
            'pagina': TinyMCE()
        }