# Generated by Django 4.0.4 on 2022-07-21 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome da empresa')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='condo/profile', verbose_name='Foto do Perfil')),
                ('street', models.CharField(blank=True, max_length=255, null=True, verbose_name='Rua')),
                ('number', models.CharField(blank=True, max_length=25, null=True, verbose_name='Numero')),
                ('district', models.CharField(blank=True, max_length=255, null=True, verbose_name='Bairro')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='Cidade')),
                ('state', models.CharField(blank=True, max_length=255, null=True, verbose_name='Estado')),
                ('cep', models.CharField(blank=True, max_length=25, null=True, verbose_name='Cep')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'companys',
                'db_table': 'company',
            },
        ),
    ]
