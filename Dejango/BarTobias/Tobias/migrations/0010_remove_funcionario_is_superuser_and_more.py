# Generated by Django 5.0.6 on 2024-05-29 20:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tobias', '0009_funcionario_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='is_superuser',
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='CPF deve conter 11 dígitos numéricos', regex='^\\d{11}$')]),
        ),
    ]
