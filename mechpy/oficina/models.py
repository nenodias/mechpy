from django.db import models
from mechpy.core.models import Pessoa

class PessoaVeiculo(models.Model):
    STATUS_DONO = "DN"
    STATUS_ANTIGO = "AT"

    STATUS = (
        (STATUS_DONO, 'Dono'),
        (STATUS_ANTIGO, 'Antigo'),
    )
    status = models.CharField('Status',max_length=2, choices=STATUS, blank=False, null=False)
    data = models.DateField('Data', auto_now_add=True, blank=True)
    ativo = models.BooleanField('Ativo', blank=True, default=True)
    km = models.IntegerField('KM')

    pessoa = models.ForeignKey(Pessoa, related_name='pessoa_veiculos', null=False, blank=False)
    veiculo = models.ForeignKey('Veiculo', related_name='pessoa_veiculos', null=False, blank=False)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        unique_together = (('pessoa', 'veiculo'))


class Marca(models.Model):

    nome = models.CharField('Nome',max_length=100, blank=False, null=False)
    descricao = models.CharField('Descrição',max_length=200)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class Modelo(models.Model):

    nome = models.CharField('Nome',max_length=100, blank=False, null=False)
    descricao = models.CharField('Descrição',max_length=200)
    ano = models.CharField('Ano',max_length=20)
    marca = models.ForeignKey('Marca', related_name='modelos')

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelo'

class Categoria(models.Model):

    nome = models.CharField('Nome',max_length=100, blank=False, null=False)
    descricao = models.CharField('Descrição',max_length=200)
    produtos = models.ManyToManyField('Produto', related_name = 'categorias')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Produto(models.Model):

    nome = models.CharField('Nome',max_length=100, blank=False, null=False)
    descricao = models.CharField('Descrição',max_length=200)
    valor = models.DecimalField('Valor',max_digits=15, decimal_places=2)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

class Cor(models.Model):

    nome = models.CharField('Nome',max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

class Veiculo(models.Model):

    observacoes = models.TextField('Observações')
    ano = models.CharField('Ano',max_length=20)
    cor = models.ForeignKey('Cor', related_name='veiculos')
    km = models.IntegerField('KM', blank=True, null=True)
    modelo = models.ForeignKey('Modelo', related_name='veiculos', null=False, blank=False)
    

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

class Servico(models.Model):

    nome = models.CharField('Nome',max_length=100, blank=False, null=False)
    descricao = models.CharField('Descrição',max_length=200)
    valor = models.DecimalField('Valor',max_digits=15, decimal_places=2)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

class Pedido(models.Model):

    descricao = models.CharField('Descrição',max_length=200)
    valor = models.DecimalField('Valor',max_digits=15, decimal_places=2)
    data_inicio = models.DateField('Data Entrada',auto_now_add=True)
    data_termino = models.DateField('Data Saída', null=True, blank=True)
    km = models.IntegerField('KM', blank=True, null=True)

    class Meta:
        abstract = True

class Item(models.Model):

    descricao = models.CharField('Descrição',max_length=200)
    valor = models.DecimalField('Valor',max_digits=15, decimal_places=2)
    quantidade = models.DecimalField('Quantidade',max_digits=15, decimal_places=2)

    class Meta:
        abstract = True

class Faturamento(models.Model):

    valor = models.DecimalField('Valor',max_digits=15, decimal_places=2)
    valor_pago = models.DecimalField('Valor',max_digits=15, decimal_places=2)
    data_pagamento = models.DateField('Data Pagamento')
    data_vencimento = models.DateField('Data Vencimento')
    juros_vencimento = models.DecimalField('Juros Vencimento',max_digits=15, decimal_places=2)

    class Meta:
        abstract = True

class PedidoVenda(Pedido):

    pessoa_veiculo = models.ForeignKey('PessoaVeiculo', related_name='pedidos_venda', null=False, blank=False)

    class Meta:
        verbose_name = 'Pedido Venda'
        verbose_name_plural = 'Pedidos Venda'

class ItemServicoVenda(Item):

    pedido_venda = models.ForeignKey('PedidoVenda', related_name='itens_servico', null=False, blank=False)
    servico = models.ForeignKey('Servico', related_name='itens_servico_venda', null=False, blank=False)

    class Meta:
        verbose_name = 'Item Serviço Venda'
        verbose_name_plural = 'Itens Serviço Venda'


class ItemProdutoVenda(Item):

    pedido_venda = models.ForeignKey('PedidoVenda', related_name='itens_produto', null=False, blank=False)
    produto = models.ForeignKey('Produto', related_name='itens_produto_venda', null=False, blank=False)
    class Meta:
        verbose_name = 'Item Produto Venda'
        verbose_name_plural = 'Itens Produto Venda'

class Funcionario(models.Model):

    nome = models.CharField('Nome',max_length=100, blank=False, null=False)
    funcao = models.CharField('Função',max_length=100, blank=False, null=False)
    data_entrada = models.DateField('Data Entrada',auto_now_add=True)
    data_saida = models.DateField('Data Saída', null=True, blank=True)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

class Apontamento(models.Model):
    descricao = models.CharField('Descrição',max_length=200, blank=False, null=False)
    data_inicio = models.DateField('Data Início',auto_now_add=True)
    data_termino = models.DateField('Data Término', null=True, blank=True)

    pedido_venda = models.ForeignKey('PedidoVenda', related_name='apontamentos', null=False, blank=False)
    servico = models.ForeignKey('Servico', related_name='apontamentos', null=False, blank=False)
    funcionario = models.ForeignKey('Funcionario', related_name='apontamentos', null=False, blank=False)

    class Meta:
        verbose_name = 'Apontamento'
        verbose_name_plural = 'Apontamentos'

class PedidoCompra(Pedido):

    pessoa_veiculo = models.ForeignKey('PessoaVeiculo', related_name='pedidos_compra', null=False, blank=False)

    class Meta:
        verbose_name = 'Pedido Compra'
        verbose_name_plural = 'Pedidos Compra'

class ItemServicoCompra(Item):

    pedido_compra = models.ForeignKey('PedidoCompra', related_name='itens_servico', null=False, blank=False)
    servico = models.ForeignKey('Servico', related_name='itens_servico_compra', null=False, blank=False)

    class Meta:
        verbose_name = 'Item Serviço Compra'
        verbose_name_plural = 'Itens Serviço Compra'


class ItemProdutoCompra(Item):

    pedido_compra = models.ForeignKey('PedidoCompra', related_name='itens_produto', null=False, blank=False)
    produto = models.ForeignKey('Produto', related_name='itens_produto_compra', null=False, blank=False)

    class Meta:
        verbose_name = 'Item Produto Compra'
        verbose_name_plural = 'Itens Produto Compra'

class FaturaRecebimento(Faturamento):
    
    pedido_venda = models.ForeignKey('PedidoVenda', related_name='faturas', null=False, blank=False)

    class Meta:
        verbose_name = 'Fatura Recebimento'
        verbose_name_plural = 'Faturas Recebimento'

class FaturaPagamento(Faturamento):

    pedido_compra = models.ForeignKey('PedidoCompra', related_name='faturas', null=False, blank=False)

    class Meta:
        verbose_name = 'Fatura Recebimento'
        verbose_name_plural = 'Faturas Recebimento'