# Generated by Django 4.0.4 on 2022-06-28 08:01

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('sistema_2', '0020_usuarios_usr_celular_usuarios_usr_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('usr_tipo', models.CharField(max_length=64)),
                ('usr_telefono', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]