# Generated by Django 4.2.7 on 2023-12-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tobias', '0006_cliente_produto_qtdproduto_delete_estoque'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='Preco',
            new_name='Preco_do_produto',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='QtdProduto',
            new_name='Quantidade_de_Produtos',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='nome',
            new_name='nome_do_produto',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='DescProduto',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='NumNotaFiscal',
        ),
        migrations.AddField(
            model_name='produto',
            name='Descricao_do_Produto',
            field=models.CharField(blank=True, db_column='DescProduto', max_length=1000),
        ),
        migrations.AddField(
            model_name='produto',
            name='Numero_de_Nota_Fiscal',
            field=models.CharField(blank=True, db_column='NumNotaFiscal', max_length=1000),
        ),
    ]
