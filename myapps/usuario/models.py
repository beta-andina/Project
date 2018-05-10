from django.db import models
from django.contrib.auth.models import User

class UserCtaCteUser(models.Model):
	iduser = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)#Uno a uno
	saldo_sin_justificar = models.DecimalField(max_digits=10, decimal_places=2)
	saldo_a_pagar = models.DecimalField(max_digits=10, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add = True)
	update_at = models.DateTimeField(auto_now= True)


	def __str__(self):
		return'{}'.format(self.iduser)


class UserCuenta_Corriente_Movimientos(models.Model): #movimientos de cuenta corriente de clientes
	iduser = models.ForeignKey(UserCtaCteUser,null = True, blank = True, on_delete=models.CASCADE) #Uno a muchos
	fecha = models.DateTimeField(auto_now= True)
	mes = models.CharField(max_length=50)
	anio = models.CharField(max_length=50)
	hora = models.CharField(max_length=50)
	tipo = models.CharField(max_length=50)
	entidad = models.CharField(max_length=50)
	comprobante = models.IntegerField()
	importe = models.DecimalField(max_digits=10, decimal_places=2)


	def __str__(self):
		return'{}'.format(self.iduser)

	