# Generated by Django 4.2.7 on 2024-04-16 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tobias', '0009_alter_funcionario_autor_alter_linkuser_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkuser',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tobias.funcionario'),
        ),
    ]
