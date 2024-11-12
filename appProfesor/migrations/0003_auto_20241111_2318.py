# Generated by Django 3.2 on 2024-11-12 02:18

import appProfesor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProfesor', '0002_auto_20241107_1314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesor',
            options={'ordering': ['nombre'], 'verbose_name': 'Profesor', 'verbose_name_plural': 'Profesores'},
        ),
        migrations.AlterField(
            model_name='profesor',
            name='dni',
            field=models.CharField(max_length=10, unique=True, validators=[appProfesor.models.validnumeros]),
        ),
        migrations.AlterModelTable(
            name='profesor',
            table='profesor',
        ),
    ]
