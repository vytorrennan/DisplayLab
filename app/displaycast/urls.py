from django.urls import path
from . import views


urlpatterns = [
    path("", views.displaycast_list, name="displaycast"),
    path("<slug:url>/", views.displaycast_detail, name="displaycast_detail"),
]
