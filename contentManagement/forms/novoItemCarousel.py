from django import forms
from main.models import ItensDoCarousel


class novoItemCarouselForm(forms.ModelForm):
    class Meta:
        model = ItensDoCarousel
        fields = "__all__"