# Generated by Django 4.2.7 on 2024-04-11 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tobias', '0010_produto_excluido_produto_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cliente',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='venda',
            name='clienteId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='listagemCliente', to='Tobias.cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venda',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='venda',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
