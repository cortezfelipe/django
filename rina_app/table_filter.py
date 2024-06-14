from django_filters import FilterSet, CharFilter, NumberFilter
from .models import Empresa, Gerencia, Setor, Status, Embarcacao, Tipo, Recursos


class EmpresaFilter(FilterSet):
    empresa = CharFilter(
        field_name='empresa', 
        lookup_expr='icontains',
        label='Empresa:'
    )
    class Meta:
        model = Empresa
        fields = ["empresa"]


class GerenciaFilter(FilterSet):
    gerencia = CharFilter(
        field_name='gerencia', 
        lookup_expr='icontains',
        label='Gerência:'
    )
    class Meta:
        model = Gerencia
        fields = ["gerencia"]


class StatusFilter(FilterSet):
    status = CharFilter(
        field_name='status', 
        lookup_expr='icontains',
        label='Status:'
    )
    class Meta:
        model = Status
        fields = ["status"]


class EmbarcacaoFilter(FilterSet):
    embarcacao = CharFilter(
        field_name='embarcacao', 
        lookup_expr='icontains',
        label='Embarcacao:'
    )
    class Meta:
        model = Embarcacao
        fields = ["embarcacao"]


class TipoFilter(FilterSet):
    tipo = CharFilter(
        field_name='tipo', 
        lookup_expr='icontains',
        label='Tipo:'
    )
    class Meta:
        model = Tipo
        fields = ["tipo"]


    
class RecursosFilter(FilterSet):
    embarcacao_id = CharFilter(
        field_name='embarcacao_id__embarcacao', 
        lookup_expr='icontains',
        label='embarcacao'
    )

    empresa_id = CharFilter(
        field_name='empresa_id__empresa', 
        lookup_expr='icontains',
        label='empresa'
    )

    gerencia_id = CharFilter(
        field_name='gerencia_id__gerencia', 
        lookup_expr='icontains',
        label='gerencia'
    )

    tipo_id = CharFilter(
        field_name='tipo_id__tipo', 
        lookup_expr='icontains',
        label='tipo'
    )

    status_id = CharFilter(
        field_name='status_id__status', 
        lookup_expr='icontains',
        label='status'
    )

    prazo_nuvem = NumberFilter(
        field_name='prazo_nuvem', 
        lookup_expr='exact',
        label='prazo'
    )

    class Meta:
        model = Recursos
        fields = ["embarcacao_id__embarcacao","empresa_id__empresa", "gerencia_id__gerencia",
                  "tipo_id__tipo", "status_id__status", "prazo_nuvem"]

class SetorFilter(FilterSet):
    setor = CharFilter(
        field_name='setor', 
        lookup_expr='icontains',
        label='Setor:'
    )

    class Meta():
        model = Setor
        fields = ["setor"]