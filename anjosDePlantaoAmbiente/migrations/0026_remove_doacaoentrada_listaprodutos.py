# Generated by Django 2.0.13 on 2019-08-28 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anjosDePlantaoAmbiente', '0025_auto_20190828_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doacaoentrada',
            name='listaProdutos',
        ),
    ]