# Generated by Django 2.2.4 on 2019-12-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_auto_20191128_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidade',
            name='sigla',
            field=models.CharField(blank=True, default='', max_length=4),
        ),
    ]