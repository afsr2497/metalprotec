# Generated by Django 4.0.4 on 2022-06-29 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_2', '0034_facturas_fac_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturas',
            name='fac_tipo_cambio',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='guias',
            name='gui_tipo_cambio',
            field=models.FloatField(default=0, null=True),
        ),
    ]