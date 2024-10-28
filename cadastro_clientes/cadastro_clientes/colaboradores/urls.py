# colaboradores/urls.py

from django.urls import path
from .views import cadastrar_colaborador, listar_colaboradores, mapa_colaboradores

urlpatterns = [
    path('cadastrar/', cadastrar_colaborador, name='cadastrar_colaborador'),
    path('listar/', listar_colaboradores, name='listar_colaboradores'),
    path('mapa/', mapa_colaboradores, name='mapa_colaboradores'),
]
