# Generated by Django 3.2 on 2024-11-12 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAlumno', '0004_alter_curso_seccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(default='nombreDefault', max_length=30),
        ),
    ]
