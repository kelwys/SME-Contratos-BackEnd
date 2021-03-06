# Generated by Django 2.2.4 on 2020-05-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0007_contrato_referencia_encerramento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='estado_contrato',
            field=models.CharField(blank=True, choices=[('EMERGENCIAL', 'Emergencial'), ('EXCEPCIONAL', 'Excepcional'), ('SUSPENSO_INTERROMPIDO', 'Suspenso / Interrompido'), ('VIGENTE', 'Vigente')], default='', max_length=30, verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='parametronotificacoesvigencia',
            name='estado_contrato',
            field=models.CharField(blank=True, choices=[('EMERGENCIAL', 'Emergencial'), ('EXCEPCIONAL', 'Excepcional'), ('SUSPENSO_INTERROMPIDO', 'Suspenso / Interrompido'), ('VIGENTE', 'Vigente')], default='', max_length=15, verbose_name='Para contratos com estado'),
        ),
    ]
