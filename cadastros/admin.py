from django.contrib import admin
from .models import Produto, Client, Shipping, ProductShip, Service, Guarantee, Term, Payment
from .forms import ClientForm   # <-- corrigido

class ProdutoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

admin.site.register(Produto, ProdutoAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'cpf', 'cnpj', 'user']   # <-- corrigido
    form = ClientForm

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

admin.site.register(Client, ClientAdmin)


class ShippingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'cnpj', 'phone']   # <-- corrigido

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

admin.site.register(Shipping, ShippingAdmin)


class ProductShipAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'deliverydays']   # <-- corrigido

admin.site.register(ProductShip, ProductShipAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'tipo', 'price', 'hourprice']   # <-- corrigido

admin.site.register(Service, ServiceAdmin)


class GuaranteeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title']   # <-- corrigido

admin.site.register(Guarantee, GuaranteeAdmin)


class TermsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title']   # <-- corrigido

admin.site.register(Term, TermsAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        '__str__', 'title', 'product', 'productDiscount', 'productInstallments',
        'service', 'serviceDiscount', 'serviceInstallments'
    ]   # <-- corrigido

admin.site.register(Payment, PaymentAdmin)
