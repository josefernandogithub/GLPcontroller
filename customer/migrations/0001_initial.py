# Generated by Django 4.0.4 on 2022-07-22 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Telefone')),
                ('street', models.CharField(blank=True, max_length=255, null=True, verbose_name='Rua')),
                ('number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Numero')),
                ('district', models.CharField(blank=True, max_length=255, null=True, verbose_name='Bairro')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customer',
                'db_table': 'customer',
            },
        ),
    ]
