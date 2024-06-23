# Generated by Django 5.0.6 on 2024-06-23 14:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCliente', models.CharField(db_column='nomeCliente', max_length=50)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProduto', models.CharField(db_column='nomeProduto', max_length=50, unique=True)),
                ('dataCadastro', models.DateTimeField(auto_now_add=True)),
                ('dataAlteracao', models.DateTimeField(auto_now=True)),
                ('precoProduto', models.FloatField(blank=True, db_column='precoProduto')),
                ('status', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acontecimento', models.CharField(db_column='acontecimento', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataVenda', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('precoTotal', models.FloatField(blank=True, default=0, null=True)),
                ('clienteId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='listagemCliente', to='Tobias.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ItemVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('precoItem', models.FloatField(blank=True, null=True)),
                ('produtoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='listagemProduto', to='Tobias.produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tobias.venda')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nome', models.CharField(max_length=30)),
                ('sobreNome', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('excluido', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, to='auth.group')),
                ('permissoes', models.ManyToManyField(blank=True, to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='venda',
            name='funcionarioId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='listagemFuncionario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Funcionario2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('funcionarioId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='idFuncionario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeFuncionario', models.CharField(blank=True, max_length=30)),
                ('enderecoFuncionario', models.CharField(blank=True, max_length=150)),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(blank=True, db_column='categoria', max_length=50)),
                ('tamanho', models.CharField(blank=True, db_column='tamanho', max_length=10)),
                ('tipo_peso', models.CharField(blank=True, db_column='tipo_peso', max_length=50)),
                ('quantidadeProduto', models.BigIntegerField(blank=True, db_column='quantidadeProduto', default=1)),
                ('dataCadastro', models.DateTimeField(auto_now_add=True)),
                ('produtoId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Tobias.produto')),
                ('cadastro', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='produtoFuncionario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='cadastro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='cadastroFuncionario', to=settings.AUTH_USER_MODEL),
        ),
    ]
