# Generated by Django 2.2.4 on 2019-11-13 22:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contratos', '0027_auto_20191113_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentofiscal',
            name='tipo_unidade',
            field=models.CharField(
                choices=[('FISCAL_DRE', 'DRE'), ('FISCAL_UNIDADE', 'UNIDADE'), ('FISCAL_OUTROS', 'OUTROS')],
                max_length=20),
        ),
    ]
