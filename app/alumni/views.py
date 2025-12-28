from django.views import View
from django.shortcuts import render

class AlumniView(View):
    def get(self, request):
        return render(request, "alumni/alumni.html")

