# Generated by Django 2.0.4 on 2018-05-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juicios', '0002_auto_20180502_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juicio',
            name='juzgado',
            field=models.CharField(choices=[('PAZ 1', 'PAZ 1'), ('PAZ 2', 'PAZ 2'), ('PAZ 3', 'PAZ 3'), ('PAZ 4', 'PAZ 4'), ('PAZ 5', 'PAZ 5'), ('PAZ 6', 'PAZ 6'), ('PAZ 7', 'PAZ 7'), ('PAZ 8', 'PAZ 8'), ('PAZ LAS HERAS', 'PAZ LAS HERAS'), ('PAZ LUJAN', 'PAZ LUJAN'), ('PAZ VILLA NUEVA', 'PAZ VILLA NUEVA')], default='PAZ 1', max_length=50),
        ),
    ]