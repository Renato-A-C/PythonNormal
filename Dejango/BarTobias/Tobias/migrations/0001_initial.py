# Generated by Django 4.2.7 on 2024-04-15 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('cpf', models.CharField(blank=True, db_column='cpfCliente', max_length=15)),
                ('cnpj', models.CharField(blank=True, db_column='cnpjCliente', max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeFuncionario', models.CharField(blank=True, max_length=30)),
                ('cpfFuncionario', models.IntegerField(blank=True)),
                ('enderecoFuncionario', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProduto', models.CharField(blank=True, db_column='nomeProduto', max_length=50)),
                ('dataCadastro', models.DateField(auto_now_add=True)),
                ('precoProduto', models.FloatField(blank=True, db_column='precoProduto')),
                ('quantidadeProduto', models.BigIntegerField(blank=True, db_column='quantidadeProduto', default=1)),
                ('status', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=75)),
                ('usuario', models.CharField(max_length=50, unique=True)),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precoTotal', models.FloatField()),
                ('status', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('clienteId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='listagemCliente', to='Tobias.cliente')),
                ('funcionarioId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='listagemFuncionario', to='Tobias.funcionario')),
                ('produtoId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='listagemProduto', to='Tobias.produto')),
            ],
        ),
        migrations.CreateModel(
            name='LinkUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
