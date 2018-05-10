from django.shortcuts import render

# Create your views here.

#VISTAS DEL GESTOR

def NuevoMovimiento2(request):
	if request.method == 'POST':
		tipo_gestor = request.POST['tipo_movimiento']
		
		if tipo_gestor == 'justificacion':

			iduser = 2
			#usuario = User.objects.filter(id=iduser)
			
			tipo = request.POST['tipo_cliente']
			juzgado = request.POST['juzgado']
			autos = request.POST['autos']
			detalle = request.POST['detalle']
			honorarios = request.POST['honorarios']
			movilidad = request.POST['movilidad']
			justificado = int(honorarios) + int(movilidad)
			s = CtaCteUser.objects.get(iduser_id = iduser)
			saldo = s.saldo_sin_justificar
			nuevo_saldo = int(saldo) - int(justificado)
			p = CtaCteUser.objects.filter(iduser_id = iduser).update(saldo_sin_justificar= nuevo_saldo)
			ctx = {'nuevo_saldo': nuevo_saldo}

		else: #si es honorarios 

			iduser = 2
			#usuario = User.objects.filter(id=iduser)
			tipo_gestor = request.POST['tipo_movimiento']
			tipo = request.POST['tipo_cliente']
			juzgado = request.POST['juzgado']
			autos = request.POST['autos']
			detalle = request.POST['detalle']
			honorarios = request.POST['honorarios']
			movilidad = request.POST['movilidad']
			justificado = int(honorarios) + int(movilidad)
			s = CtaCteUser.objects.get(iduser_id = iduser)
			saldo = s.saldo_a_pagar
			nuevo_saldo = int(saldo) + int(justificado)
			p = CtaCteUser.objects.filter(iduser_id = iduser).update(saldo_a_pagar= nuevo_saldo)
			ctx = {'nuevo_saldo': nuevo_saldo}



	else:
		ctx = {'mensaje': 'NO DATOS'}
	return render(request, 'gestor/gestor_form.html', ctx)

