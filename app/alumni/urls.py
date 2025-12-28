from django.urls import path
from .views import AlumniView

urlpatterns = [
    path('', AlumniView.as_view(), name='alumni'),
]
