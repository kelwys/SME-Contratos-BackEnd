# Generated by Django 2.2.4 on 2020-05-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0003_unidade_sigla'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidade',
            name='bairro',
            field=models.CharField(max_length=50, default='', blank=True),
        ),
        migrations.AddField(
            model_name='unidade',
            name='logradouro',
            field=models.CharField(max_length=100, default='', blank=True),
        ),
    ]
