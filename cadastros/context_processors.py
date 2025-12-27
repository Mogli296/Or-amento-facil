# -*- coding: utf-8 -*-
"""
Context processors para a app cadastros.
Apenas adiciona variáveis simples ao contexto global dos templates.
"""

def cadastros(request):
    if request.user.is_authenticated:
        return {
            'verUser': True,
            'user_id': request.user.id,
        }
    else:
        return {
            'verUser': False,
            'padrao': "Você precisa estar logado para ver isso.",
        }
