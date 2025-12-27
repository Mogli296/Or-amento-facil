# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator
from .models import Client, Produto, Shipping

# Validador simples para telefones brasileiros
phone_validator = RegexValidator(
    regex=r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$',
    message="Número de telefone inválido. Use o formato (XX) XXXXX-XXXX."
)

# =========================
# Formulário de Cliente
# =========================
class ClientForm(forms.ModelForm):
    phone = forms.CharField(
        validators=[phone_validator],
        required=False,
        label="Telefone"
    )
    celphone = forms.CharField(
        validators=[phone_validator],
        required=False,
        label="Celular"
    )

    class Meta:
        model = Client
        fields = '__all__'

# =========================
# Formulário de Produto
# =========================
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

# =========================
# Formulário de Frete
# =========================
class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = '__all__'
