# Generated by Django 3.2 on 2024-11-07 16:14

import appProfesor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProfesor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='dni',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='telefono',
            field=models.CharField(max_length=30),
        ),
    ]
