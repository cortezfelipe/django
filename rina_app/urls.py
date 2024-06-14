
from django.urls import path
from rina_app.views import (
    edit_setor, index, logout_view, recursos_empresa, 
    edit_empresa, recursos_gerencia, edit_gerencia,
    recursos_status, edit_status, edit_embarcacao, recursos_embarcacao,
    recursos_tipo, edit_tipo, recursos, edit_recursos, setor
)
# from django.conf.urls.static import static
# from django.conf import settings

app_name = 'rina_app'

urlpatterns = [
    path('', index, name='index'),
    path('logout', logout_view, name='logout'),
    path('recursos/empresa', recursos_empresa, name='recursos_empresa'),
    path('edit/empresa', edit_empresa, name='edit_empresa'),
    path('recursos/gerencia', recursos_gerencia, name='recursos_gerencia'),
    path('edit/gerencia', edit_gerencia, name='edit_gerencia'),
    path('recursos/status', recursos_status, name='recursos_status'),
    path('edit/status', edit_status, name='edit_status'),
    path('recursos/embarcacao', recursos_embarcacao, name='recursos_embarcacao'),
    path('edit/embarcacao', edit_embarcacao, name='edit_embarcacao'),
    path('recursos/tipo', recursos_tipo, name='recursos_tipo'),
    path('edit/tipo', edit_tipo, name='edit_tipo'),
    path('recursos', recursos, name='recursos'),
    path('edit/recursos', edit_recursos, name='edit_recursos'),
    path('setor', setor, name='setor'),
    path('edit/setor', edit_setor, name='edit_setor'),



]