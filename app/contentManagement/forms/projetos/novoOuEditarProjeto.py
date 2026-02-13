from django import forms
from projetos.models import Projeto
from tinymce.widgets import TinyMCE


class novoOuEditarProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto
        fields = ["titulo", "oculto", "capa", "dataHora", "resumo", "pagina"]
        widgets = {
            'dataHora': forms.DateTimeInput(),
            'resumo': forms.Textarea(),
            'pagina': TinyMCE()
        }
