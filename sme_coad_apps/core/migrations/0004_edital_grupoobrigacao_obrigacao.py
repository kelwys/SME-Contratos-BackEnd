# Generated by Django 2.2.4 on 2020-05-27 19:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_unidade_sigla'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('numero', models.CharField(max_length=100, verbose_name='Número do Edital')),
            ],
            options={
                'verbose_name': 'Edital',
                'verbose_name_plural': 'Editais',
            },
        ),
        migrations.CreateModel(
            name='GrupoObrigacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Grupo')),
                ('edital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupos_de_obrigacoes', to='core.Edital')),
            ],
            options={
                'verbose_name': 'Grupo de Obrigação',
                'verbose_name_plural': 'Grupos de Obrigações',
            },
        ),
        migrations.CreateModel(
            name='Obrigacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('item', models.CharField(max_length=15)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obrigacoes', to='core.GrupoObrigacao')),
            ],
            options={
                'verbose_name': 'Obrigação',
                'verbose_name_plural': 'Obrigações',
            },
        ),
    ]
