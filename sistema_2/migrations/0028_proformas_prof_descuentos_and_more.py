# Generated by Django 4.0.4 on 2022-06-29 15:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_2', '0027_alter_productos_pro_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proformas',
            name='prof_descuentos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(default=0), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='proformas',
            name='prof_cliente',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='proformas',
            name='prof_estado',
            field=models.CharField(default='NoGenerada', max_length=64),
        ),
        migrations.AlterField(
            model_name='proformas',
            name='prof_fecha',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='proformas',
            name='prof_productos',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), null=True, size=None), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='proformas',
            name='prof_valor_total',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='proformas',
            name='prof_vendedor',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), null=True, size=None),
        ),
    ]