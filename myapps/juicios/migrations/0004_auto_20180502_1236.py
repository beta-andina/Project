# Generated by Django 2.0.4 on 2018-05-02 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juicios', '0003_auto_20180502_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juicio',
            name='auto',
            field=models.CharField(max_length=6),
        ),
    ]
