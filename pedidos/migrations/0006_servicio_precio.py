# Generated by Django 4.0 on 2021-12-29 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_calidad_calificacion_fecha_genero_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='precio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
