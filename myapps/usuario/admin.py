from django.contrib import admin
from myapps.usuario.models import UserCtaCteUser, UserCuenta_Corriente_Movimientos

class UserCtaCteUserAdmin(admin.ModelAdmin):
    list_display = ('iduser', 'saldo_sin_justificar', 'saldo_a_pagar')
   	


admin.site.register(UserCtaCteUser,UserCtaCteUserAdmin)
admin.site.register(UserCuenta_Corriente_Movimientos)
