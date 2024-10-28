# cadastro_clientes/clientes/urls.py

from django.urls import path
from .views import cadastrar_empresa, mapa_empresas, listar_empresas

urlpatterns = [
    path('cadastrar/', cadastrar_empresa, name='cadastrar_empresa'),
    path('listar/', listar_empresas, name='listar_empresas'),
    path('mapa/', mapa_empresas, name='mapa_empresas'),

]
