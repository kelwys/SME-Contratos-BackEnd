from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from brazilnum.cnpj import format_cnpj
from django.core.validators import MinLengthValidator
from django.db import models

from ...core.models_abstracts import ModeloBase, TemNome


class Empresa(ModeloBase, TemNome):
    historico = AuditlogHistoryField()

    # TODO Implementar validação do CNPJ para não permitir gravação de CNPJ inválido.
    cnpj = models.CharField('CNPJ', validators=[MinLengthValidator(14)], max_length=14, unique=True)

    def __str__(self):
        return self.nome

    @property
    def cnpj_formatado(self):
        return format_cnpj(self.cnpj)

    class Meta:
        verbose_name = 'Empresa Contratada'
        verbose_name_plural = 'Empresas Contratadas'


auditlog.register(Empresa)
