# Generated by Django 2.0.4 on 2018-04-27 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Cliente',
        ),
        migrations.RenameModel(
            old_name='Client_checking_account',
            new_name='Cuenta_Corriente',
        ),
        migrations.RenameModel(
            old_name='Client_checking_account_movements',
            new_name='Cuenta_Corriente_Movimientos',
        ),
    ]
