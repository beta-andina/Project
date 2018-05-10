from django.db import models
from myapps.clientes.models import Cliente
from django.contrib.auth.models import User

# Create your models here.
class Juicio(models.Model):

	JUZGADOS_CHOICES = (
			('PAZ 1','PAZ 1'),
			('PAZ 2','PAZ 2'),
			('PAZ 3','PAZ 3'),
			('PAZ 4','PAZ 4'),
			('PAZ 5','PAZ 5'),
			('PAZ 6','PAZ 6'),
			('PAZ 7','PAZ 7'),
			('PAZ 8','PAZ 8'),
			('PAZ LAS HERAS','PAZ LAS HERAS'),
			('PAZ LUJAN','PAZ LUJAN'),
			('PAZ VILLA NUEVA','PAZ VILLA NUEVA'),
	)


	idcliente =  models.ForeignKey(Cliente,null = True, blank = True, on_delete=models.CASCADE) #Uno a muchos
	auto = models.CharField(max_length=6)
	juzgado = models.CharField(max_length=50, choices=JUZGADOS_CHOICES, default='PAZ 1')
	n_cuenta_1 = models.CharField(max_length=50, null=True, blank=True)
	n_cuenta_2 = models.CharField(max_length=50, null=True, blank=True)
	endoso = models.CharField(max_length=50)
	fecha_inicio = models.DateTimeField(max_length=15, null=True, blank=True)
	idlistado = models.IntegerField()
	idorden = models.IntegerField()
	empresa = models.CharField(max_length=50)
	estado = models.CharField(max_length=50, default = 'NORMAL')
	observacion = models.CharField(max_length=500, default = 'SIN OBSERVACION')
	created_at = models.DateTimeField(auto_now_add = True)
	update_at = models.DateTimeField(auto_now= True)
	usuario = models.CharField(max_length=50, default = User)

	def __str__(self):
		return'{} {}'.format(self.auto, self.juzgado)

class Juicio_Movimiento(models.Model):
	idjuicio = models.ForeignKey(Juicio ,null = True, blank = True, on_delete=models.CASCADE) #Uno a muchos
	auto = models.CharField(max_length=50)
	juzgado = models.CharField(max_length=50)
	tipo = models.CharField(max_length=50)
	importe = models.DecimalField(max_digits=10, decimal_places=2)
	observacion = models.CharField(max_length=500)
	created_at = models.DateTimeField(auto_now_add = True)
	update_at = models.DateTimeField(auto_now= True)
	usuario = models.CharField(max_length=50)

	def __str__(self):
		return'{} {}'.format(self.auto, self.juzgado)

class Juicio_Tarea(models.Model):
	idjuicio = models.ForeignKey(Juicio ,null = True, blank = True, on_delete=models.CASCADE) #Uno a muchos
	auto = models.CharField(max_length=50)
	juzgado = models.CharField(max_length=50)
	estado = models.CharField(max_length=50, default = 'SIN VISAR')
	visado = models.DateTimeField(max_length=15, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add = True)
	update_at = models.DateTimeField(auto_now= True)
	usuario = models.CharField(max_length=50)

	def __str__(self):
		return'{} {}'.format(self.auto, self.juzgado)



