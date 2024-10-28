# cadastro_clientes/clientes/forms.py

from django import forms
from .models import Empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj', 'endereco', 'numero', 'complemento', 'cep', 'cidade', 'estado', 'telefone', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),  # Input de texto padrão
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),  # Input de texto padrão
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),  # Textarea
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),  # Input de texto padrão
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  # Input de e-mail
        }
