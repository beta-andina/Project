from django.contrib import admin
from myapps.clientes.models import Cliente, Cuenta_Corriente, Cuenta_Corriente_Movimientos, Cliente_imagen

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('idcliente', 'nombre', 'apellido')
    search_fields = ('nombre', 'apellido', 'documento')
    list_per_page = 25

class CtaCteAdmin(admin.ModelAdmin):
    list_display = ('idcliente', 'saldo_a_vencer', 'saldo_vencido','deuda_total','tipo_atraso','cuotas_atrasadas')
    search_fields = ('idcliente','tipo_atraso', 'cuotas_atrasadas')
    list_per_page = 25

class Cliente_Imagen_Admin(admin.ModelAdmin):
    list_display = ('idcliente', 'tipo', 'imagen','created_at')
    search_fields = ('idcliente','tipo')
    list_per_page = 25   

# Register your models here.
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Cuenta_Corriente, CtaCteAdmin)
admin.site.register(Cuenta_Corriente_Movimientos)
admin.site.register(Cliente_imagen,Cliente_Imagen_Admin)
