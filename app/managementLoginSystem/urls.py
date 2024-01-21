from django.urls import path
from . import views

urlpatterns = [
    path("login", views.userLogin.as_view(), name='login'),
    path("signup", views.userSignup.as_view(), name='signup'),
    path("logout", views.userLogout.as_view(), name='logout'),
]
