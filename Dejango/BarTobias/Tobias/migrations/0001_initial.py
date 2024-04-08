# Generated by Django 4.2.7 on 2024-04-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_column='nomeCliente', max_length=50)),
                ('cpf', models.CharField(blank=True, db_column='cpfCliente', max_length=15)),
                ('cnpj', models.CharField(blank=True, db_column='cnpjCliente', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_do_produto', models.CharField(blank=True, db_column='nomeProduto', max_length=30)),
                ('dataCadastro', models.DateField(auto_now_add=True)),
                ('Descricao_do_Produto', models.CharField(blank=True, db_column='DescProduto', max_length=1000)),
                ('Preco_do_produto', models.FloatField(blank=True, db_column='Preco', default=1)),
                ('Numero_de_Nota_Fiscal', models.CharField(blank=True, db_column='NumNotaFiscal', max_length=1000)),
                ('Quantidade_de_Produtos', models.BigIntegerField(blank=True, db_column='Qtd', default=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
