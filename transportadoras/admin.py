from django.contrib import admin
from .models import Cnpj          # <-- corrigido
from .forms import CnpjForm       # <-- corrigido

class CnpjAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'cnpj']  # usa __str__ em vez de __unicode__
    form = CnpjForm

admin.site.register(Cnpj, CnpjAdmin)
