from django.urls import path
from .views import ListaNoticias

urlpatterns = [
    path('', ListaNoticias.as_view(), name='ListaNoticias'),
]