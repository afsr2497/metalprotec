# Generated by Django 4.0.4 on 2022-06-29 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_2', '0032_guias_gui_descuentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturas',
            name='fac_fecha_vencimiento',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='facturas',
            name='fac_gui_codigo',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
