from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.core import serializers


import json

from rina_app.forms import EmpresaForm, GerenciaForm, SetorForm, StatusForm, EmbarcacaoForm, TipoForm, RecursosForm, RecursosFormFilter
from rina_app.models import Empresa, Gerencia, Setor, Status, Embarcacao, Tipo, Recursos
from rina_app.tables import EmpresaTable, GerenciaTable, SetorTable, StatusTable, EmbarcacaoTable, TipoTable, RecursosTable
from rina_app.table_filter import EmpresaFilter, GerenciaFilter, SetorFilter, StatusFilter, EmbarcacaoFilter, TipoFilter, RecursosFilter

# Create your views here.

def add_item(request, form, url_redirect):
    # Form POST adicionar
    form_obj = form(request.POST)   

    if form_obj.is_valid():
        form_obj.save()
    
    return HttpResponseRedirect(url_redirect)


def delet_item(request, model):

    j_request = json.loads(json.dumps(request.POST))
    obj_id = j_request["id"]
    model_obj = get_object_or_404(model, pk=obj_id)
    model_obj.delete()

    return JsonResponse({
        "success": 'true'
    })
    

def get_item_data(request, model):

    j_request = json.loads(json.dumps(request.POST))
    obj_id = j_request["id"]

    model_obj = get_object_or_404(model, pk=obj_id)
    
    return JsonResponse(
        serializers.serialize('json', [model_obj]),
        safe=False)


def filter_tables(request, model, model_table, model_filter):
    filter = model_filter(request.GET, queryset=model.objects.all())
    table = model_table(filter.qs)
    table.paginate(page=request.GET.get("page", 1), per_page=10)    
    return (filter.form, table)


@login_required
def index(request):

    if request.method == "POST":
        form_empresa = EmpresaForm(request.POST)   
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        if form_empresa.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            print(form_empresa.cleaned_data.values())
            form_empresa.save()
        
        return HttpResponseRedirect("/")

    # if a GET (or any other method) we'll create a blank form
    
    else:
        form_empresa = EmpresaForm()
        form_gerencia = GerenciaForm()   
        form_status = StatusForm()
        forms_recursos = RecursosForm()
        return render(request, "rina_app/index.html", {
            "form": form_empresa, 'form_gerencia': form_gerencia,
            "form_status": form_status,
            'forms_recursos': forms_recursos
            })
   

@login_required
def recursos_empresa(request):

    if request.method == "GET":

        form_empresa = EmpresaForm()
        (filter, table) = filter_tables(request, Empresa, EmpresaTable, EmpresaFilter)

        return render(request, "rina_app/form_input_view_template.html", {
            "form": form_empresa,
            "form_page_title": "Empresas",
            "table": table,
            "edit_form": form_empresa,
            "action_url": reverse_lazy('rina_app:edit_empresa'),
            "filter_form": filter
            })



@login_required
def edit_empresa(request):

    j_request = json.loads(json.dumps(request.POST))
    
    if request.method == "POST" and 'input' in request.POST:
        return add_item(request, EmpresaForm, reverse_lazy('rina_app:recursos_empresa'))
    
    # Form POST editar
    elif request.method == "POST" and 'edit' in request.POST:
        form_empresa = EmpresaForm(request.POST)   

        if form_empresa.is_valid():

            empresa_id = form_empresa.cleaned_data.get('data_id')
            empresa_obj = get_object_or_404(Empresa, pk=empresa_id)
            empresa_obj.empresa = form_empresa.cleaned_data.get('empresa')
            empresa_obj.save()

            return HttpResponseRedirect(reverse_lazy('rina_app:recursos_empresa'))

    #AJAX POST deletar
    elif request.method == "POST" and j_request['action'] == 'delete':        
        return delet_item(request, Empresa)
    
    #AJAX POST ler
    elif request.method == "POST" and j_request['action'] == 'get-data':
        
        return get_item_data(request, Empresa)


@login_required
def recursos_gerencia(request):

    if request.method == "GET":
        form_gerencia = GerenciaForm()
        (filter, table) = filter_tables(request, Gerencia, GerenciaTable, GerenciaFilter)

        return render(request, "rina_app/form_input_view_template.html", {
            "form": form_gerencia,
            "form_page_title": "Gerência",
            "table": table,
            "edit_form": form_gerencia,
            "action_url": reverse_lazy('rina_app:edit_gerencia'),
            "filter_form": filter
            })


@login_required
def edit_gerencia(request):

    j_request = json.loads(json.dumps(request.POST))

    # Form POST adicionar
    if request.method == "POST" and 'input' in request.POST:
        return add_item(request, GerenciaForm, reverse_lazy('rina_app:recursos_gerencia'))
    
    # Form POST editar
    elif request.method == "POST" and 'edit' in request.POST:
        form_gerencia = GerenciaForm(request.POST)   

        if form_gerencia.is_valid():

            gerencia_id = form_gerencia.cleaned_data.get('data_id')
            gerencia_obj = get_object_or_404(Gerencia, pk=gerencia_id)
            gerencia_obj.gerencia = form_gerencia.cleaned_data.get('gerencia')
            gerencia_obj.save()

            return HttpResponseRedirect(reverse_lazy('rina_app:recursos_gerencia'))

    #AJAX POST deletar
    elif request.method == "POST" and j_request['action'] == 'delete':        
        return delet_item(request, Gerencia)

    #AJAX POST ler
    elif request.method == "POST" and j_request['action'] == 'get-data':
        return get_item_data(request, Gerencia)


@login_required
def recursos_status(request):

    if request.method == "GET":
        form = StatusForm()
        (filter, table) = filter_tables(request, Status, StatusTable, StatusFilter)
        
        return render(request, "rina_app/form_input_view_template.html", {
            "form": form,
            "form_page_title": "Status",
            "table": table,
            "edit_form": form,
            "action_url": reverse_lazy('rina_app:edit_status'),
            "filter_form": filter
            })
    

@login_required
def edit_status(request):

    j_request = json.loads(json.dumps(request.POST))

    # Form POST adicionar
    if request.method == "POST" and 'input' in request.POST:
        return add_item(request, StatusForm, reverse_lazy('rina_app:recursos_status'))
    
    # Form POST editar
    elif request.method == "POST" and 'edit' in request.POST:
        form_status = StatusForm(request.POST)

        if form_status.is_valid():

            status_id = form_status.cleaned_data.get('data_id')
            status_obj = get_object_or_404(Status, pk=status_id)
            status_obj.status = form_status.cleaned_data.get('status')
            status_obj.save()

            return HttpResponseRedirect(reverse_lazy('rina_app:recursos_status'))

    #AJAX POST deletar
    elif request.method == "POST" and j_request['action'] == 'delete':        
        return delet_item(request, Status)

    #AJAX POST ler
    elif request.method == "POST" and j_request['action'] == 'get-data':
        return get_item_data(request, Status)


@login_required
def recursos_embarcacao(request):

    if request.method == "GET":
        form = EmbarcacaoForm()
        (filter, table) = filter_tables(request, Embarcacao, EmbarcacaoTable, EmbarcacaoFilter)
        
        return render(request, "rina_app/form_input_view_template.html", {
            "form": form,
            "form_page_title": "Embarcação",
            "table": table,
            "edit_form": form,
            "action_url": reverse_lazy('rina_app:edit_embarcacao'),
            "filter_form": filter
            })
    

@login_required
def edit_embarcacao(request):

    j_request = json.loads(json.dumps(request.POST))

    # Form POST adicionar
    if request.method == "POST" and 'input' in request.POST:
        return add_item(request, EmbarcacaoForm, reverse_lazy('rina_app:recursos_embarcacao'))
    
    # Form POST editar
    elif request.method == "POST" and 'edit' in request.POST:
        form_embarcacao = EmbarcacaoForm(request.POST)

        if form_embarcacao.is_valid():

            status_id = form_embarcacao.cleaned_data.get('data_id')
            status_obj = get_object_or_404(Embarcacao, pk=status_id)
            status_obj.embarcacao = form_embarcacao.cleaned_data.get('embarcacao')
            status_obj.save()

            return HttpResponseRedirect(reverse_lazy('rina_app:recursos_embarcacao'))

    #AJAX POST deletar
    elif request.method == "POST" and j_request['action'] == 'delete':
        return delet_item(request, Embarcacao)

    #AJAX POST ler
    elif request.method == "POST" and j_request['action'] == 'get-data':
        return get_item_data(request, Embarcacao)


@login_required
def recursos_tipo(request):

    if request.method == "GET":
        form = TipoForm()
        (filter, table) = filter_tables(request, Tipo, TipoTable, TipoFilter)

        return render(request, "rina_app/form_input_view_template.html", {
            "form": form,
            "form_page_title": "Tipos",
            "table": table,
            "edit_form": form,
            "action_url": reverse_lazy('rina_app:edit_tipo'),
            "filter_form": filter
            })


@login_required
def edit_tipo(request):

    j_request = json.loads(json.dumps(request.POST))

    # Form POST adicionar
    if request.method == "POST" and 'input' in request.POST:
        return add_item(request, TipoForm, reverse_lazy('rina_app:recursos_tipo'))
    
    # Form POST editar
    elif request.method == "POST" and 'edit' in request.POST:
        form_tipo = TipoForm(request.POST)

        if form_tipo.is_valid():

            tipo_id = form_tipo.cleaned_data.get('data_id')
            status_obj = get_object_or_404(Tipo, pk=tipo_id)
            status_obj.tipo = form_tipo.cleaned_data.get('tipo')
            status_obj.save()

            return HttpResponseRedirect(reverse_lazy('rina_app:recursos_tipo'))

    #AJAX POST deletar
    elif request.method == "POST" and j_request['action'] == 'delete':
        return delet_item(request, Tipo)

    #AJAX POST ler
    elif request.method == "POST" and j_request['action'] == 'get-data':
        return get_item_data(request, Tipo)


@login_required
def recursos(request):
    if request.method == "GET":
        form = RecursosForm()
        recursos_filter = RecursosFormFilter()
        (filter, table) = filter_tables(request, Recursos, RecursosTable, RecursosFilter)

        return render(request, "rina_app/form_input_view_template.html", {
            "form": form,
            "form_page_title": "Recursos",
            "table": table,
            "edit_form": form,
            "action_url": reverse_lazy('rina_app:edit_recursos'),
            "filter_form": recursos_filter
            })


@login_required
def edit_recursos(request):
    j_request = json.loads(json.dumps(request.POST))

    # Form POST adicionar
    if request.method == "POST" and 'input' in request.POST:
        return add_item(request, RecursosForm, reverse_lazy('rina_app:recursos'))
    
    # Form POST editar
    elif request.method == "POST" and 'edit' in request.POST:
        form_recurso = RecursosForm(request.POST)

        if form_recurso.is_valid():

            recursos_id = form_recurso.cleaned_data.get('data_id')
            recursos_obj = get_object_or_404(Recursos, pk=recursos_id)
            recursos_obj.tipo_id = form_recurso.cleaned_data.get('tipo_id')
            recursos_obj.embarcacao_id = form_recurso.cleaned_data.get('embarcacao_id')
            recursos_obj.empresa_id = form_recurso.cleaned_data.get('empresa_id')
            recursos_obj.gerencia_id = form_recurso.cleaned_data.get('gerencia_id')
            recursos_obj.status_id = form_recurso.cleaned_data.get('status_id')
            recursos_obj.prazo_nuvem = form_recurso.cleaned_data.get('prazo_nuvem')
            recursos_obj.save()

            return HttpResponseRedirect(reverse_lazy('rina_app:recursos'))

    #AJAX POST deletar
    elif request.method == "POST" and j_request['action'] == 'delete':
        return delet_item(request, Recursos)

    #AJAX POST ler
    elif request.method == "POST" and j_request['action'] == 'get-data':
        return get_item_data(request, Recursos)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))

@login_required
def setor(request): #Talvez tenha que adicionar 'recursos'

    if request.method == 'GET':
        form = SetorForm()
        (filter, table) = filter_tables(request, Setor, SetorTable, SetorFilter)

        return render(request, 'rina_app/form_input_view_template.html', {
            'form': form,
            'form_page_title': 'setor',
            'table': table,
            'edit_form': form,
            'action_url': reverse_lazy('rina_app:edit_setor'),
            'filter_form': filter
            })

@login_required
def edit_setor(request):

    j_request = json.loads(json.dumps(request.POST))

    # Form POST adicionar
    if request.method == 'POST' and 'input' in request.POST:
        return add_item(request, SetorForm, reverse_lazy('rina_app:setor')) #Talvez tenha que adicionar 'recursos'

    # Form POST editar
    elif request.method == 'POST' and 'edit' in request.POST:
        form = SetorForm(request.POST)

        if form.is_valid():

           id = form.cleaned_data.get('data_id')
           obj = get_object_or_404(Setor, pk=id)
           obj.setor = form.cleaned_data.get('setor')
           obj.save()

           return HttpResponseRedirect(reverse_lazy('rina_app:setor')) #Talvez tenha que adicionar 'recursos'

    #AJAX POST deletar
    elif request.method == 'POST' and j_request['action'] == 'delete':
        return delet_item(request, Setor)

    #AJAX POST ler
    elif request.method == 'POST' and j_request['action'] == 'get-data':
        return get_item_data(request, Setor)