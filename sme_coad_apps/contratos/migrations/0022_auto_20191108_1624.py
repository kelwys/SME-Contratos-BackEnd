# Generated by Django 2.2.4 on 2019-11-08 19:24

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('contratos', '0021_auto_20191108_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colunascontrato',
            name='colunas_array',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True,
                                                                 default=[{'field': 'termo_contrato', 'header': 'TC'},
                                                                          {'field': 'processo', 'header': 'Processo'},
                                                                          {'field': 'tipo_servico.nome',
                                                                           'header': 'Tipo de Serviço'},
                                                                          {'field': 'empresa_contratada.nome',
                                                                           'header': 'Empresa'},
                                                                          {'field': 'estado_contrato',
                                                                           'header': 'Estado do Contrato'},
                                                                          {'field': 'data_encerramento',
                                                                           'header': 'Data Encerramento'}],
                                                                 verbose_name='Lista de campos'),
        ),
    ]
