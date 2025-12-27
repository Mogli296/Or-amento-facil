# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django_tables2 import RequestConfig

from .models import Produto, Client, Shipping
from .forms import ProdutoForm, ClientForm, ShippingForm

# =========================
# Views principais
# =========================

@login_required
def cadastros(request):
    template = 'cadastros.html'
    context = {'template_name': 'add_clients.html'}
    return render(request, template, context)


@login_required
def add_produtos(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return HttpResponseRedirect(reverse('cadastros'))
    return render(request, "add_produtos.html", {"form": form})


@login_required
def delete_produtos(request, id):
    produto = Produto.objects.get(id=id, user=request.user)
    produto.delete()
    return HttpResponseRedirect(reverse('cadastros'))


@login_required
def edit_produtos(request, id):
    instance = Produto.objects.get(id=id, user=request.user)
    form = ProdutoForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cadastros'))
    return render(request, "single_produto.html", {"form": form, "edit": True})


@login_required
def add_clients(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return HttpResponseRedirect(reverse('cadastros'))
    return render(request, "add_clients.html", {"form": form, "form_name": "Cadastre seu cliente"})


@login_required
def edit_clients(request, id):
    instance = Client.objects.get(id=id, user=request.user)
    form = ClientForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cadastros'))
    return render(request, "edit_clients.html", {"form": form, "edit": True})


@login_required
def delete_clients(request, id):
    client = Client.objects.get(id=id, user=request.user)
    client.delete()
    return HttpResponseRedirect(reverse('cadastros'))


@login_required
def edit_shippings(request, id):
    instance = Shipping.objects.get(id=id, user=request.user)
    form = ShippingForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cadastros'))
    return render(request, "edit_shippings.html", {"form": form, "edit": True})


@login_required
def delete_shippings(request, id):
    shipping = Shipping.objects.get(id=id, user=request.user)
    shipping.delete()
    return HttpResponseRedirect(reverse('cadastros'))


# =========================
# Placeholders para futuras views
# =========================

@login_required
def add_shippings(request):
    return render(request, "add_shippings.html")

@login_required
def add_services(request):
    return render(request, "add_services.html")

@login_required
def add_terms(request):
    return render(request, "add_terms.html")

@login_required
def add_garantia(request):
    return render(request, "add_garantia.html")
