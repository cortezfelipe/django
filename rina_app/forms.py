from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit, Fieldset, Layout, Row, Column
from crispy_forms.bootstrap import InlineField

from .models import Empresa, Gerencia, Setor, Status, Recursos, Embarcacao, Tipo


class BaseFormRinaApp(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'gerencia-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.form_tag = False
    
    data_id = forms.CharField(widget=forms.HiddenInput(), required=False)



class EmpresaForm(BaseFormRinaApp):
    
    # data_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Empresa
        fields = ["id", "empresa", "ativo"]


class GerenciaForm(BaseFormRinaApp):

    # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Gerencia
        fields = ["gerencia", "ativo"]

    
class StatusForm(BaseFormRinaApp):

    class Meta:
        model = Status
        fields = ["status", "ativo"]


class EmbarcacaoForm(BaseFormRinaApp):

    class Meta:
        model = Embarcacao
        fields = ["embarcacao", "ativo"]


class TipoForm(BaseFormRinaApp):

    class Meta:
        model = Tipo
        fields = ["tipo", "ativo"]


class RecursosForm(BaseFormRinaApp):

    class Meta:
        model = Recursos
        fields = ["id", "embarcacao_id","empresa_id", "gerencia_id",
                  "tipo_id", "status_id", "prazo_nuvem"]

    def __init__(self, *args, **kwargs):
        super(RecursosForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('embarcacao_id', css_class='form-group col-md-6 mb-0'),
                Column('empresa_id', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('gerencia_id', css_class='form-group col-md-6 mb-0'),
                Column('tipo_id', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('status_id', css_class='form-group col-md-6 mb-0'),
                Column('prazo_nuvem', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            )
        )


class RecursosFormFilter(RecursosForm):
    
    embarcacao_id = forms.CharField(label="Embarcação", required=False)
    empresa_id = forms.CharField(label="Empresa", required=False)
    gerencia_id = forms.CharField(label="Gerencia", required=False)
    tipo_id = forms.CharField(label="Tipo", required=False)
    status_id = forms.CharField(label="Status", required=False)
    prazo_nuvem = forms.IntegerField(label="Prazo Nuvem", required=False)

    class Meta:
        model = Recursos
        fields = ["id", "embarcacao_id","empresa_id", "gerencia_id",
                  "tipo_id", "status_id", "prazo_nuvem"]

class SetorForm(BaseFormRinaApp):

    class Meta:
        model = Setor
        fields = ["id", "setor"]        


