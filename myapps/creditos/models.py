from django.db import models
from myapps.clientes.models import Cliente

# Create your models here.
class Orden(models.Model):
	idorden = models.IntegerField()
	idcliente = models.ForeignKey(Cliente ,null = True, blank = True, on_delete=models.CASCADE) #Uno a muchos
	fecha_inicio =  models.DateTimeField(auto_now_add = True)
	cantidad_cuotas = models.IntegerField()
	capital =  models.IntegerField()
	producido = models.IntegerField()
	empresa = models.CharField(max_length=50)
	idgarante = models.IntegerField()
	idvendedor = models.CharField(max_length=50)
	forma_de_pago = models.CharField(max_length=50)
	estado = models.CharField(max_length=50)
	observacion = models.CharField(max_length=200)
	monto_facturacion = models.DecimalField(max_digits=10, decimal_places=2)
	fecha_facturacion = models.DateTimeField(auto_now_add = True)
	numero_factura = models.IntegerField()
	cft = models.DecimalField(max_digits=10, decimal_places=2)
	cft2 = models.DecimalField(max_digits=10, decimal_places=2)
	tea = models.DecimalField(max_digits=10, decimal_places=2)
	tea2 = models.DecimalField(max_digits=10, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add = True)
	update_at = models.DateTimeField(auto_now= True)
	usuario = models.CharField(max_length=50)

class Cuota(models.Model):
	idorden = models.ForeignKey(Orden ,null = True, blank = True, on_delete=models.CASCADE) #Uno a muchos
	monto_cuota = models.DecimalField(max_digits=10, decimal_places=2)
	saldo_cuota = models.DecimalField(max_digits=10, decimal_places=2)
	fecha_cuota = models.DateTimeField(auto_now_add = True)
	mes_cuota = models.CharField(max_length=50)
	anio_cuota = models.CharField(max_length=50)
	interes = models.DecimalField(max_digits=10, decimal_places=2)
	capital = models.DecimalField(max_digits=10, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add = True)
	update_at = models.DateTimeField(auto_now= True)
	
