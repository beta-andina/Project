# Generated by Django 2.0.4 on 2018-04-27 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcliente', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('documento', models.CharField(max_length=8)),
                ('cuil', models.CharField(max_length=13)),
                ('fecha_nacimiento', models.DateField()),
                ('movil', models.CharField(max_length=20)),
                ('tel_laboral', models.CharField(max_length=20)),
                ('descripcion_tel_laboral', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=500)),
                ('localidad', models.CharField(max_length=50)),
                ('distrito', models.CharField(max_length=50)),
                ('codigo_postal', models.CharField(max_length=4)),
                ('email', models.EmailField(max_length=75)),
                ('banco_pago', models.CharField(max_length=20)),
                ('sucursal', models.CharField(max_length=10)),
                ('n_cuenta', models.CharField(max_length=15)),
                ('cbu', models.CharField(blank=True, max_length=50, null=True)),
                ('trabajo', models.CharField(max_length=50)),
                ('tipo_cliente', models.CharField(default='NORMAL', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('fecha_baja', models.DateTimeField(blank=True, max_length=15, null=True)),
                ('usuario', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Client_checking_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deuda_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo_a_vencer', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo_vencido', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_atraso', models.CharField(max_length=50)),
                ('cuotas_atrasadas', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('idcliente', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Client_checking_account_movements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('mes', models.CharField(max_length=50)),
                ('anio', models.CharField(max_length=50)),
                ('hora', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('entidad', models.CharField(max_length=50)),
                ('comprobante', models.IntegerField()),
                ('importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo_anterior', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo_actual', models.DecimalField(decimal_places=2, max_digits=10)),
                ('idcliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Client_checking_account')),
            ],
        ),
    ]
