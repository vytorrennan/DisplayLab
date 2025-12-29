from django.views import View
from django.shortcuts import render
from .models import Aluno

class AlumniView(View):
    def get(self, request):
        return render(request, "alumni/alumni.html")

class ListaAlumni(View):
    def get(self, request):
        alunos_db = Aluno.objects.all()
        print(alunos_db)

        context = {
            'alunos': alunos_db,
            'title': 'Lista de Alunos'
        }
        return render(request, "alumni/alumni.html", context)
