from django.db import models
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class BaseDimension(models.Model):

    id = models.AutoField(primary_key=True)
    ativo = models.IntegerField(
        default = 1,
        choices = [(0, "Não"), (1, "Sim")]
    )

    class Meta():
        abstract = True


class Empresa(BaseDimension):
    # id = models.AutoField(primary_key=True)
    empresa = models.CharField(max_length=200, verbose_name="Empresa")

    def __str__(self):
        return self.empresa
    
    class Meta():
        db_table = "qua_empresa"


class Gerencia(BaseDimension):
    # id = models.AutoField(primary_key=True)
    gerencia = models.CharField(max_length=200, verbose_name="Gerência")

    def __str__(self):
        return self.gerencia
    
    class Meta():
        db_table = "qua_gerencia"


class Status(BaseDimension):
    # id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=200, verbose_name="Status")

    def __str__(self):
        return self.status
    
    class Meta():
        db_table = "qua_status_recurso"


class Embarcacao(BaseDimension):
    # id = models.AutoField(primary_key=True)
    embarcacao = models.CharField(max_length=200, verbose_name="Embarcação")

    def __str__(self):
        return self.embarcacao
    
    class Meta():
        db_table = "qua_embarcacao"


class Tipo(BaseDimension):
    # id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=200, verbose_name="Tipo")

    def __str__(self):
        return self.tipo
    
    class Meta():
        db_table = "qua_tipo"


class Recursos(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_id = models.ForeignKey(Tipo, on_delete=models.CASCADE, verbose_name="Tipo")
    embarcacao_id = models.ForeignKey(Embarcacao, on_delete=models.CASCADE, verbose_name="Embarcação")
    empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE,verbose_name="Empresa")
    gerencia_id = models.ForeignKey(Gerencia, on_delete=models.CASCADE, verbose_name="Gerência")
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Status")
    prazo_nuvem = models.IntegerField(verbose_name="Prazo Nuvem")


    class Meta():
        db_table = "qua_recurso"


    
class Setor(models.Model):
    id = models.AutoField(primary_key=True)
    setor = models.CharField(max_length=200)

    class Meta():
        db_table = "setor"

