from django.urls import path
from .views import ListaAlumni

urlpatterns = [
    path('', ListaAlumni.as_view(), name='alumni'),
]
