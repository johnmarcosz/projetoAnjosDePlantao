# Generated by Django 2.0.13 on 2019-07-12 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anjosDePlantaoAmbiente', '0007_auto_20190712_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixageral',
            name='saldo',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='doacaoentrada',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='doacaosaida',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True),
        ),
    ]
