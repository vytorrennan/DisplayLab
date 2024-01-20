from django.urls import path
from . import views


urlpatterns = [
    path("revista/", views.revista.as_view(), name="revista"),
    path("revista/<slug:url>/", views.paginaDePost.as_view(), name="paginaDePost"),
]