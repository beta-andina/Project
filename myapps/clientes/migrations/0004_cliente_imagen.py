# Generated by Django 2.0.4 on 2018-05-09 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20180427_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente_imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(choices=[('DNI', 'DNI'), ('IMPUESTO', 'IMPUESTO'), ('BONO', 'BONO'), ('MOVIMIENTOS_CBU', 'MOVIMIENTOS_CBU'), ('OTROS', 'OTROS')], default='BONO', max_length=50)),
                ('imagen', models.ImageField(upload_to='uploads/')),
                ('idcliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente')),
            ],
        ),
    ]
