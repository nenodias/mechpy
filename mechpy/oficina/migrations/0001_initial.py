# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apontamento',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=200)),
                ('data_inicio', models.DateField(verbose_name='Data Início', auto_now_add=True)),
                ('data_termino', models.DateField(verbose_name='Data Término', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Apontamentos',
                'verbose_name': 'Apontamento',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
                'verbose_name': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cores',
                'verbose_name': 'Cor',
            },
        ),
        migrations.CreateModel(
            name='FaturaPagamento',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('valor', models.DecimalField(verbose_name='Valor', max_digits=15, decimal_places=2)),
                ('valor_pago', models.DecimalField(verbose_name='Valor', max_digits=15, decimal_places=2)),
                ('data_pagamento', models.DateField(verbose_name='Data Pagamento')),
                ('data_vencimento', models.DateField(verbose_name='Data Vencimento')),
                ('juros_vencimento', models.DecimalField(verbose_name='Juros Vencimento', max_digits=15, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Faturas Recebimento',
                'verbose_name': 'Fatura Recebimento',
            },
        ),
        migrations.CreateModel(
            name='FaturaRecebimento',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('valor', models.DecimalField(verbose_name='Valor', max_digits=15, decimal_places=2)),
                ('valor_pago', models.DecimalField(verbose_name='Valor', max_digits=15, decimal_places=2)),
                ('data_pagamento', models.DateField(verbose_name='Data Pagamento')),
                ('data_vencimento', models.DateField(verbose_name='Data Vencimento')),
                ('juros_vencimento', models.DecimalField(verbose_name='Juros Vencimento', max_digits=15, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Faturas Recebimento',
                'verbose_name': 'Fatura Recebimento',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('funcao', models.CharField(verbose_name='Função', max_length=100)),
                ('data_entrada', models.DateField(verbose_name='Data Entrada', auto_now_add=True)),
                ('data_saida', models.DateField(verbose_name='Data Saída', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Funcionários',
                'verbose_name': 'Funcionário',
            },
        ),
        migrations.CreateModel(
            name='ItemProdutoCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=200)),
                ('valor', models.DecimalField(verbose_name='Valor', max_digits=15, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Itens Produto Compra',
                'verbose_name': 'Item Produto Compra',
            },
        ),
        migrations.CreateModel(
            name='ItemProdutoVenda',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=200)),
                ('valor', models.DecimalField(verbose_name='Valor', max_digits=15, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Itens Produto Venda',
                'verbose_name': 'Item Produto Venda',
            },
        ),
        migrations.CreateModel(
            name='ItemServicoCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=200)),
                ('valor', models.DecimalField(verbose_name='Valor', max_digits=15, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Itens Serviço Compra',
                'verbose_name': 'Item Serviço Compra',
            },
        ),
        migrations.CreateModel(
            name='ItemServicoVenda',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=200)),
                ('valor', models.DecimalField(verbose_name='Valor', max_digits=15, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Itens Serviço Venda',
                'verbose_name': 'Item Serviço Venda',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Marcas',
                'verbose_name': 'Marca',
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=200)),
                ('ano', models.CharField(verbose_name='Ano', max_length=20)),
                ('marca', models.ForeignKey(related_name='modelos', to='oficina.Marca')),
            ],
            options={
                'verbose_name_plural': 'Modelo',
                'verbose_name': 'Modelo',
            },
        ),
        migrations.CreateModel(
            name='PedidoCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=200)),
                ('valor', models.DecimalField(verbose_name='Valor', max_digits=15, decimal_places=2)),
                ('data_inicio', models.DateField(verbose_name='Data Entrada', auto_now_add=True)),
                ('data_termino', models.DateField(verbose_name='Data Saída', blank=True, null=True)),
                ('km', models.IntegerField(verbose_name='KM', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Pedidos Compra',
                'verbose_name': 'Pedido Compra',
            },
        ),
        migrations.CreateModel(
            name='PedidoVenda',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=200)),
                ('valor', models.DecimalField(verbose_name='Valor', max_digits=15, decimal_places=2)),
                ('data_inicio', models.DateField(verbose_name='Data Entrada', auto_now_add=True)),
                ('data_termino', models.DateField(verbose_name='Data Saída', blank=True, null=True)),
                ('km', models.IntegerField(verbose_name='KM', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Pedidos Venda',
                'verbose_name': 'Pedido Venda',
            },
        ),
        migrations.CreateModel(
            name='PessoaVeiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('status', models.CharField(verbose_name='Status', choices=[('DN', 'Dono'), ('AT', 'Antigo')], max_length=2)),
                ('data', models.DateField(verbose_name='Data', auto_now_add=True)),
                ('ativo', models.BooleanField(verbose_name='Ativo', default=True)),
                ('km', models.IntegerField(verbose_name='KM')),
                ('pessoa', models.ForeignKey(related_name='pessoa_veiculos', to='core.Pessoa')),
            ],
            options={
                'verbose_name_plural': 'Marcas',
                'verbose_name': 'Marca',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=200)),
                ('valor', models.DecimalField(verbose_name='Valor', max_digits=15, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Produtos',
                'verbose_name': 'Produto',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=200)),
                ('valor', models.DecimalField(verbose_name='Valor', max_digits=15, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Serviços',
                'verbose_name': 'Serviço',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('observacoes', models.TextField(verbose_name='Observações')),
                ('ano', models.CharField(verbose_name='Ano', max_length=20)),
                ('km', models.IntegerField(verbose_name='KM', blank=True, null=True)),
                ('cor', models.ForeignKey(related_name='veiculos', to='oficina.Cor')),
                ('modelo', models.ForeignKey(related_name='veiculos', to='oficina.Modelo')),
            ],
            options={
                'verbose_name_plural': 'Produtos',
                'verbose_name': 'Produto',
            },
        ),
        migrations.AddField(
            model_name='pessoaveiculo',
            name='veiculo',
            field=models.ForeignKey(related_name='pessoa_veiculos', to='oficina.Veiculo'),
        ),
        migrations.AddField(
            model_name='pedidovenda',
            name='pessoa_veiculo',
            field=models.ForeignKey(related_name='pedidos_venda', to='oficina.PessoaVeiculo'),
        ),
        migrations.AddField(
            model_name='pedidocompra',
            name='pessoa_veiculo',
            field=models.ForeignKey(related_name='pedidos_compra', to='oficina.PessoaVeiculo'),
        ),
        migrations.AddField(
            model_name='itemservicovenda',
            name='pedido_venda',
            field=models.ForeignKey(related_name='itens_servico', to='oficina.PedidoVenda'),
        ),
        migrations.AddField(
            model_name='itemservicovenda',
            name='servico',
            field=models.ForeignKey(related_name='itens_servico_venda', to='oficina.Servico'),
        ),
        migrations.AddField(
            model_name='itemservicocompra',
            name='pedido_compra',
            field=models.ForeignKey(related_name='itens_servico', to='oficina.PedidoCompra'),
        ),
        migrations.AddField(
            model_name='itemservicocompra',
            name='servico',
            field=models.ForeignKey(related_name='itens_servico_compra', to='oficina.Servico'),
        ),
        migrations.AddField(
            model_name='itemprodutovenda',
            name='pedido_venda',
            field=models.ForeignKey(related_name='itens_produto', to='oficina.PedidoVenda'),
        ),
        migrations.AddField(
            model_name='itemprodutovenda',
            name='produto',
            field=models.ForeignKey(related_name='itens_produto_venda', to='oficina.Produto'),
        ),
        migrations.AddField(
            model_name='itemprodutocompra',
            name='pedido_compra',
            field=models.ForeignKey(related_name='itens_produto', to='oficina.PedidoCompra'),
        ),
        migrations.AddField(
            model_name='itemprodutocompra',
            name='produto',
            field=models.ForeignKey(related_name='itens_produto_compra', to='oficina.Produto'),
        ),
        migrations.AddField(
            model_name='faturarecebimento',
            name='pedido_venda',
            field=models.ForeignKey(related_name='faturas', to='oficina.PedidoVenda'),
        ),
        migrations.AddField(
            model_name='faturapagamento',
            name='pedidoCompra',
            field=models.ForeignKey(related_name='faturas', to='oficina.PedidoCompra'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='produtos',
            field=models.ManyToManyField(related_name='categorias', to='oficina.Produto'),
        ),
        migrations.AddField(
            model_name='apontamento',
            name='funcionario',
            field=models.ForeignKey(related_name='apontamentos', to='oficina.Funcionario'),
        ),
        migrations.AddField(
            model_name='apontamento',
            name='pedido_venda',
            field=models.ForeignKey(related_name='apontamentos', to='oficina.PedidoVenda'),
        ),
        migrations.AddField(
            model_name='apontamento',
            name='servico',
            field=models.ForeignKey(related_name='apontamentos', to='oficina.Servico'),
        ),
        migrations.AlterUniqueTogether(
            name='pessoaveiculo',
            unique_together=set([('pessoa', 'veiculo')]),
        ),
    ]
