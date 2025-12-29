from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

# Importando os modelos e os formulários que você enviou
from alumni.models import Aluno, edicao
from contentManagement.forms.alumni.novoOuEditarForm import AlunoForm
from contentManagement.forms.alumni.novoOuEditarAlumni import EdicaoForm
from contentManagement.views.viewsHome import rangePages

@method_decorator(login_required, name="dispatch")
class novoAluno(View):
    """View para cadastrar um novo Aluno (Egresso)."""
    def get(self, request):
        form = AlunoForm()
        return render(request, "basicForm.html", {"form": form, "label": "Novo Aluno"})

    def post(self, request):
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Aluno cadastrado com sucesso!")
            return redirect("editarAluno")
        return render(request, "basicForm.html", {"form": form, "label": "Novo Aluno"})

@method_decorator(login_required, name="dispatch")
class editarAluno(View):
    context = {}
    """View para listar os Alunos cadastrados."""
    def get(self, request):
        # Ordenação por nome
        aluno_list = Aluno.objects.all().order_by("nome")
        paginator = Paginator(aluno_list, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        self.context["rangePages"] = rangePages(9, page_obj)
        self.context["page_obj"] = page_obj
        return render(request, "editarAluno.html", self.context)

@method_decorator(login_required, name="dispatch")
class editarAlunoId(View):
    """View para editar ou excluir um Aluno específico."""
    def get(self, request, id):
        aluno_instance = get_object_or_404(Aluno, id=id)
        form = AlunoForm(instance=aluno_instance)
        return render(request, "basicForm.html", {"form": form, "label": f"Editando Aluno: {aluno_instance.nome}"})

    def post(self, request, id):
        aluno_instance = get_object_or_404(Aluno, id=id)
        
        if "delete" in request.POST:
            aluno_instance.delete()
            messages.success(request, "Registro de Aluno excluído.")
            return redirect("editarAluno")
            
        form = AlunoForm(request.POST, request.FILES, instance=aluno_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados do Aluno atualizados.")
            return redirect("editarAluno")
            
        return render(request, "basicForm.html", {"form": form, "label": f"Editando Aluno: {aluno_instance.nome}"})

@method_decorator(login_required, name="dispatch")
class novaEdicao(View):
    """View para cadastrar uma nova Edição de Alumni."""
    def get(self, request):
        form = EdicaoForm()
        return render(request, "basicForm.html", {"form": form, "label": "Nova Edição"})

    def post(self, request):
        form = EdicaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Edição cadastrada com sucesso!")
            return redirect("contentManagement") # Ou uma página de listagem de edições
        return render(request, "basicForm.html", {"form": form, "label": "Nova Edição"})