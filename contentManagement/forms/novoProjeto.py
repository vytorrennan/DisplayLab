from django import forms
from projetos.models import Projeto
from tinymce.widgets import TinyMCE


class novoProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ["titulo", "capa", "resumo", "pagina"]
        widgets = {
            'resumo': forms.Textarea(),
            'pagina': TinyMCE()
        }
    
    #url = forms.CharField(label="Url", max_length=250, widget=forms.TextInput())
    #titulo = forms.CharField(label="Titulo", max_length=250, widget=forms.TextInput())
    #capa = forms.CharField(label="Capa", max_length=512, widget=forms.TextInput())
    #resumo = forms.CharField(label="Resumo", max_length=1000, widget=forms.Textarea(attrs={"rows":"6"}))
    #pagina = forms.CharField(label="Pagina", widget=forms.Textarea(attrs={"rows":"30"}))
