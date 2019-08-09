# Generated by Django 2.0.13 on 2019-07-10 17:05

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
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data', models.DateTimeField()),
                ('local', models.CharField(max_length=80)),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=60)),
                ('estado', models.CharField(max_length=20)),
                ('observacoes', models.TextField()),
                ('dataDeCadastro', models.DateTimeField(blank=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
