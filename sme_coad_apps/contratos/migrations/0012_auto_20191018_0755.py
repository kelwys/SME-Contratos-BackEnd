# Generated by Django 2.2.4 on 2019-10-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0011_contrato_data_encerramento'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='tem_ceu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contrato',
            name='tem_ua',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contrato',
            name='tem_ue',
            field=models.BooleanField(default=False),
        ),
    ]
