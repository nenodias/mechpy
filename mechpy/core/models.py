from django.db import models
from django.contrib.auth import get_user_model

class Pessoa(models.Model):

    TIPO_PESSOA_FISICA = 'PF'
    TIPO_PESSOA_JURIDICA = 'PJ'

    TIPO_PESSOA = (
        (TIPO_PESSOA_FISICA, 'Pessoa Física'),
        (TIPO_PESSOA_JURIDICA, 'Pessoa Jurídica'),
    )

    nome = models.CharField('Nome',max_length=200, blank=False, null=False)
    observacao = models.TextField('Observação', blank=True, null=True)
    telefone = models.CharField('Telefone',max_length=20, blank=True, null=True)
    celular = models.CharField('Celular',max_length=20, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    tipo = models.CharField('Tipo',max_length=2, blank=False, null=False, choices=TIPO_PESSOA)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

class PessoaFisica(models.Model):
    pessoa = models.OneToOneField(
        Pessoa,
        verbose_name='Pessoa Física',
        related_name='pessoa_fisica',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    rg = models.CharField('RG',max_length=20)
    cpf = models.IntegerField('CPF', blank=True, null=True)

    class Meta:
        verbose_name = 'Pessoa Física'
        verbose_name_plural = 'Pessoas Físicas'

class PessoaJuridica(models.Model):

    pessoa = models.OneToOneField(
        Pessoa,
        verbose_name='Pessoa Jurídica',
        related_name='pessoa_juridica',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    cnpj = models.IntegerField('CNPJ', blank=True, null=True)
    razao_social = models.CharField('Razão Social',max_length=200)
    nome_fantasia = models.CharField('Nome Fantasia',max_length=200)
    descricao = models.CharField('Descrição',max_length=200)
    inscricao_estadual = models.CharField('Inscrição Estadual',max_length=30)
    inscricao_municipal = models.CharField('Inscrição Municipal',max_length=30)

    class Meta:
        verbose_name = 'Pessoa Jurídica'
        verbose_name_plural = 'Pessoas Jurídicas'

class Contato(models.Model):
    nome = models.CharField('Nome',max_length=20)
    email = models.EmailField('Email', blank=True, null=True)
    telefone = models.CharField('Telefone',max_length=20)
    pessoa = models.ForeignKey('Pessoa', related_name='contatos')

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

class Pais(models.Model):

    nome = models.CharField('Nome',max_length=100, blank=False, null=False)
    sigla = models.CharField('Sigla',max_length=2, blank=False, null=False)
    
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'

class Estado(models.Model):

    nome = models.CharField('Nome',max_length=100, blank=False, null=False)
    sigla = models.CharField('Sigla',max_length=2, blank=False, null=False)
    pais = models.ForeignKey('Pais', related_name='estados')
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


class Cidade(models.Model):

    nome = models.CharField('Nome',max_length=100, blank=False, null=False)
    codigo_ibge = models.CharField('Código IBGE',max_length=30, blank=True, null=True)
    estado = models.ForeignKey('Estado', related_name='cidades')

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

class Endereco(models.Model):

    nome = models.CharField('Nome',max_length=100, blank=False, null=False)
    numero = models.CharField('Número', max_length=50)
    rua = models.CharField('Rua', max_length=100)
    bairro = models.CharField('Bairro', max_length=100)
    cep = models.CharField('Cep', max_length=20)
    cidade = models.OneToOneField('Cidade', verbose_name='Cidade')
    pessoa = models.ForeignKey('Pessoa', related_name='enderecos')

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'