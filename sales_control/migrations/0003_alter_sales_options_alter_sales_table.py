# Generated by Django 4.0.4 on 2022-08-30 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_control', '0002_rename_salles_sales'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name': 'Venda', 'verbose_name_plural': 'Vendas'},
        ),
        migrations.AlterModelTable(
            name='sales',
            table='sales',
        ),
    ]