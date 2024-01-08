from django.urls import path
from . import views


urlpatterns = [
    path("revista/", views.revista, name="revista"),
]