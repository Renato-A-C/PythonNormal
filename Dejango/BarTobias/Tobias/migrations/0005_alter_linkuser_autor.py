# Generated by Django 4.2.7 on 2024-04-16 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tobias', '0004_rename_first_name_customuser_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkuser',
            name='autor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
