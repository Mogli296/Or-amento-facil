# -*- coding: utf-8 -*-
from django import forms
from localflavor.br.forms import BRCNPJField   # corrigido
from .models import Cnpj                       # corrigido

class CnpjForm(forms.ModelForm):
    cnpj = BRCNPJField(label='CNPJ', required=False)

    class Meta:
        model = Cnpj
        fields = ['user', 'cnpj']   # ajuste conforme os campos que você quer no form
