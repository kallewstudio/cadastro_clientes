# cadastro_clientes/clientes/urls.py

from django.urls import path
from .views import cadastrar_empresa

urlpatterns = [
    path('cadastrar/', cadastrar_empresa, name='cadastrar_empresa'),
]
