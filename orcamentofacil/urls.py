# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from orcamentos.views import base
from cadastros import views as cadastros_views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Página inicial
    path('', base, name='base'),

    # Cadastros
    path('cadastros/', cadastros_views.cadastros, name='cadastros'),
    path('members/<str:username>/', cadastros_views.add_produtos, name='add_produtos'),
    path('cadastros/produto/<int:id>/', cadastros_views.deletar, name='deletar'),
    path('cadastros/client/<int:id>/', cadastros_views.delete_clients, name='delete_clients'),
    path('cadastros/shipping/<int:id>/', cadastros_views.delete_shippings, name='delete_shippings'),
    path('single_produto/<int:id>/', cadastros_views.edit_produtos, name='edit_produtos'),
    path('edit_clients/<int:id>/', cadastros_views.edit_clients, name='edit_clients'),
    path('add_clients/', cadastros_views.add_clients, name='add_clients'),
    path('add_shippings/', cadastros_views.add_shippings, name='add_shippings'),
    path('edit_shippings/<int:id>/', cadastros_views.edit_shippings, name='edit_shippings'),

    # Accounts (django-registration)
    path('accounts/', include('registration.backends.default.urls')),
]
