from django import forms
from main.models import carouselItem


class novoOuEditarItemCarouselForm(forms.ModelForm):
    class Meta:
        model = carouselItem
        fields = "__all__"