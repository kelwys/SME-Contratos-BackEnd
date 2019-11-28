# Generated by Django 2.2.4 on 2019-11-28 20:44

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColunasContrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('colunas_array', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=[{'field': 'termo_contrato', 'header': 'TC'}, {'field': 'processo', 'header': 'Processo'}, {'field': 'tipo_servico.nome', 'header': 'Tipo de Serviço'}, {'field': 'empresa_contratada.nome', 'header': 'Empresa'}, {'field': 'estado_contrato', 'header': 'Estado do Contrato'}, {'field': 'data_encerramento', 'header': 'Data Encerramento'}], verbose_name='Lista de campos')),
            ],
            options={
                'verbose_name': 'Colunas do Usuário',
                'verbose_name_plural': 'Colunas do Usuário',
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('termo_contrato', models.CharField(max_length=20, unique=True, verbose_name='TC No.')),
                ('processo', models.CharField(blank=True, default='', max_length=50)),
                ('objeto', models.TextField(blank=True, default='')),
                ('data_assinatura', models.DateField(blank=True, null=True, verbose_name='data da assinatura')),
                ('data_ordem_inicio', models.DateField(blank=True, null=True, verbose_name='data da ordem de início')),
                ('vigencia_em_dias', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('situacao', models.CharField(choices=[('ATIVO', 'Ativo'), ('ENCERRADO', 'Encerrado'), ('RASCUNHO', 'Rascunho')], default='RASCUNHO', max_length=15)),
                ('observacoes', models.TextField(blank=True, default='')),
                ('estado_contrato', models.CharField(blank=True, choices=[('EMERGENCIAL', 'Emergencial'), ('EXCEPCIONAL', 'Excepcional'), ('ULTIMO_ANO', 'Último Ano'), ('VIGENTE', 'Vigente')], default='', max_length=15, verbose_name='estado')),
                ('data_encerramento', models.DateField(blank=True, null=True)),
                ('tem_ue', models.BooleanField(default=False)),
                ('tem_ua', models.BooleanField(default=False)),
                ('tem_ceu', models.BooleanField(default=False)),
                ('dotacao_orcamentaria', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, verbose_name='Dotação Orçamentária'), blank=True, default=list, size=None)),
            ],
            options={
                'verbose_name': 'Contrato',
                'verbose_name_plural': 'Contratos',
            },
        ),
        migrations.CreateModel(
            name='ContratoUnidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('valor_mensal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('valor_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('lote', models.CharField(blank=True, default='', max_length=20)),
                ('dre_lote', models.CharField(blank=True, default='', max_length=5, verbose_name='DRE do lote')),
            ],
            options={
                'verbose_name': 'Unidade de Contrato',
                'verbose_name_plural': 'Unidades de Contratos',
            },
        ),
        migrations.CreateModel(
            name='DocumentoFiscal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('anexo', models.FileField(upload_to='uploads/')),
                ('tipo_unidade', models.CharField(choices=[('FISCAL_DRE', 'DRE'), ('FISCAL_UNIDADE', 'UNIDADE'), ('FISCAL_OUTROS', 'OUTROS')], max_length=20)),
            ],
            options={
                'verbose_name': 'Documento Fiscal',
                'verbose_name_plural': 'Documentos Fiscais',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=160, verbose_name='Nome')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('cnpj', models.CharField(max_length=14, unique=True, validators=[django.core.validators.MinLengthValidator(14)], verbose_name='CNPJ')),
            ],
            options={
                'verbose_name': 'Empresa Contratada',
                'verbose_name_plural': 'Empresas Contratadas',
            },
        ),
        migrations.CreateModel(
            name='TipoServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('nome', models.CharField(max_length=160, unique=True, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Tipo de Serviço',
                'verbose_name_plural': 'Tipos de Serviço',
            },
        ),
        migrations.CreateModel(
            name='ParametroNotificacoesVigencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('estado_contrato', models.CharField(blank=True, choices=[('EMERGENCIAL', 'Emergencial'), ('EXCEPCIONAL', 'Excepcional'), ('ULTIMO_ANO', 'Último Ano'), ('VIGENTE', 'Vigente')], default='', max_length=15, verbose_name='Para contratos com estado')),
                ('vencendo_em', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Vencendo a partir de (dias)')),
                ('repetir_notificacao_a_cada', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Repetir notificação a cada (dias)')),
            ],
            options={
                'verbose_name': 'Parâmetro de notificação de vigência',
                'verbose_name_plural': 'Parâmetros de notificação de vigência',
                'unique_together': {('estado_contrato', 'vencendo_em')},
            },
        ),
        migrations.CreateModel(
            name='ObrigacaoContratual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('item', models.CharField(max_length=15)),
                ('obrigacao', models.TextField(default='')),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obrigacoes_contratuais', to='contratos.Contrato')),
            ],
            options={
                'verbose_name': 'Obrigação Contratual',
                'verbose_name_plural': 'Obrigações Contratuais',
            },
        ),
        migrations.CreateModel(
            name='NotificacaoVigenciaContrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificacoes_vigencia', to='contratos.Contrato')),
            ],
            options={
                'verbose_name': 'Notificação de vigência de contrato',
                'verbose_name_plural': 'Notificações de vigência de contrato',
            },
        ),
    ]
