from django.contrib import admin
from myapps.clientes.models import Cliente, Cuenta_Corriente, Cuenta_Corriente_Movimientos

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Cuenta_Corriente)
admin.site.register(Cuenta_Corriente_Movimientos)
