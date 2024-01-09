from django import forms
from revista.models import Revista
from tinymce.widgets import TinyMCE


class novoPostRevistaForm(forms.ModelForm):
    class Meta:
        model = Revista
        fields = ["url", "titulo", "capa", "resumo", "pagina"]
        widgets = {
            'pagina': TinyMCE()
        }