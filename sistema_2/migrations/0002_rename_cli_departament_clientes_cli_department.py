# Generated by Django 4.0.4 on 2022-06-17 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='cli_departament',
            new_name='cli_department',
        ),
    ]
