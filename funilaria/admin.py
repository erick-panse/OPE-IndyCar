from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Empresa)
admin.site.register(Orcamento)
admin.site.register(OrdemDeServico)

