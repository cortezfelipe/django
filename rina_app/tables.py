import django_tables2 as tables

from rina_app.models import Empresa, Gerencia, Setor, Status, Embarcacao, Tipo, Recursos

def get_url(view_name):
        from django.urls import reverse_lazy
        return reverse_lazy(view_name)


class BaseRinaAppTable(tables.Table):
    edit_html = '<a class="edit-item" href="#"><i class="fa fa-edit"></i></a>'
    delete_html = '<a class="delete-item" href="#"><i class="fa fa-trash"></i></a>'
    col_edit = tables.TemplateColumn(edit_html)
    col_delete = tables.TemplateColumn(delete_html)
    col_edit.verbose_name = ""
    col_delete.verbose_name = ""
    col_edit.attrs = {"td":{"style" : "width:5%;" }}
    col_delete.attrs = {"td":{"style" : "width:5%;" }}
    
    



class EmpresaTable(BaseRinaAppTable):
    
    class Meta:
        model = Empresa
        fields = ("col_edit", "col_delete",  "id", "empresa", "ativo")
        row_attrs = {
            "data-id": lambda record: record.pk,
            "data-view": get_url('rina_app:edit_empresa')
        }


class GerenciaTable(BaseRinaAppTable):

    class Meta:
        model = Gerencia
        fields = ("col_edit", "col_delete",  "id", "gerencia", "ativo")
        row_attrs = {
            "data-id": lambda record: record.pk,
            "data-view": get_url('rina_app:edit_gerencia')
        }


class StatusTable(BaseRinaAppTable):

    class Meta:
        model = Status
        fields = ("col_edit", "col_delete",  "id", "status", "ativo")
        row_attrs = {
            "data-id": lambda record: record.pk,
            "data-view": get_url('rina_app:edit_status')
        }
        
        attrs = {
            'th': {
                'class': 'table-links', 
            },
        }


class EmbarcacaoTable(BaseRinaAppTable):

    class Meta:
        model = Embarcacao
        fields = ("col_edit", "col_delete",  "id", "embarcacao", "ativo")
        row_attrs = {
            "data-id": lambda record: record.pk,
            "data-view": get_url('rina_app:edit_embarcacao')
        }


class TipoTable(BaseRinaAppTable):

    class Meta:
        model = Tipo
        fields = ("col_edit", "col_delete",  "id", "tipo", "ativo")
        row_attrs = {
            "data-id": lambda record: record.pk,
            "data-view": get_url('rina_app:edit_tipo')
        }
    

class RecursosTable(BaseRinaAppTable):

    class Meta:
        model = Recursos
        fields = ("col_edit", "col_delete","id", "tipo_id", "embarcacao_id",
                  "empresa_id", "gerencia_id", "status_id", "prazo_nuvem")
        row_attrs = {
            "data-id": lambda record: record.pk,
            "data-view": get_url('rina_app:edit_recursos')
        }

class SetorTable(BaseRinaAppTable):

    class Meta():
        model = Setor
        fields = ("col_edit","col_delete","id", "setor")

        row_attrs = {
            'data-id': lambda record: record.pk,
            'data-view': get_url('rina_app:edit_setor')
        }        

