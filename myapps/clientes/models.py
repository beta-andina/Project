from django.db import models

# Create your models here.
class Cliente(models.Model):
	idcliente = models.IntegerField()
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	documento = models.CharField(max_length=8)
	cuil = models.CharField(max_length=13)
	fecha_nacimiento = models.DateField()
	movil = models.CharField(max_length=20)
	tel_laboral = models.CharField(max_length=20)
	descripcion_tel_laboral = models.CharField(max_length=50)
	domicilio = models.CharField(max_length=500)
	localidad = models.CharField(max_length=50)
	distrito = models.CharField(max_length=50)
	codigo_postal = models.CharField(max_length=4)
	email = models.EmailField(max_length=75)
	banco_pago = models.CharField(max_length=20)
	sucursal = models.CharField(max_length=10)
	n_cuenta = models.CharField(max_length=15)
	cbu = models.CharField(max_length=50, null=True, blank=True)
	trabajo = models.CharField(max_length=50)
	tipo_cliente = models.CharField(max_length=50, default='NORMAL')
	created_at = models.DateTimeField(auto_now_add = True)
	update_at = models.DateTimeField(auto_now= True)
	fecha_baja = models.DateTimeField(max_length=15, null=True, blank=True)
	usuario = models.CharField(max_length = 25)
	



	def __str__(self):
		return'{} {}'.format(self.nombre, self.apellido)


class Cuenta_Corriente(models.Model): #cuenta corriente de clientes
	idcliente = models.OneToOneField(Cliente,null = True, blank = True, on_delete=models.CASCADE) #Uno a uno
	deuda_total = models.DecimalField(max_digits=10, decimal_places=2)
	saldo_a_vencer = models.DecimalField(max_digits=10, decimal_places=2)
	saldo_vencido = models.DecimalField(max_digits=10, decimal_places=2)
	tipo_atraso = models.CharField(max_length=50, default='SIN ATRASO')
	cuotas_atrasadas = models.IntegerField(default='0')
	created_at = models.DateTimeField(auto_now_add = True)
	update_at = models.DateTimeField(auto_now= True)

	def __str__(self):
		return'{}'.format(self.idcliente)



class Cuenta_Corriente_Movimientos(models.Model): #movimientos de cuenta corriente de clientes
	idcliente = models.ForeignKey(Cuenta_Corriente,null = True, blank = True, on_delete=models.CASCADE) #Uno a muchos
	fecha = models.DateTimeField(auto_now= True)
	mes = models.CharField(max_length=50)
	anio = models.CharField(max_length=50)
	hora = models.CharField(max_length=50)
	tipo = models.CharField(max_length=50)
	entidad = models.CharField(max_length=50)
	comprobante = models.IntegerField()
	importe = models.DecimalField(max_digits=10, decimal_places=2)
	saldo_anterior = models.DecimalField(max_digits=10, decimal_places=2)
	saldo_actual =	models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return'{}'.format(self.idcliente)
