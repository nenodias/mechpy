# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-14 00:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apontamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('data_inicio', models.DateField(auto_now_add=True, verbose_name='Data Início')),
                ('data_termino', models.DateField(blank=True, null=True, verbose_name='Data Término')),
            ],
            options={
                'verbose_name': 'Apontamento',
                'verbose_name_plural': 'Apontamentos',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Cor',
                'verbose_name_plural': 'Cores',
            },
        ),
        migrations.CreateModel(
            name='FaturaPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('data_pagamento', models.DateField(verbose_name='Data Pagamento')),
                ('data_vencimento', models.DateField(verbose_name='Data Vencimento')),
                ('juros_vencimento', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Juros Vencimento')),
            ],
            options={
                'verbose_name': 'Fatura Recebimento',
                'verbose_name_plural': 'Faturas Recebimento',
            },
        ),
        migrations.CreateModel(
            name='FaturaRecebimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('data_pagamento', models.DateField(verbose_name='Data Pagamento')),
                ('data_vencimento', models.DateField(verbose_name='Data Vencimento')),
                ('juros_vencimento', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Juros Vencimento')),
            ],
            options={
                'verbose_name': 'Fatura Recebimento',
                'verbose_name_plural': 'Faturas Recebimento',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('funcao', models.CharField(max_length=100, verbose_name='Função')),
                ('data_entrada', models.DateField(auto_now_add=True, verbose_name='Data Entrada')),
                ('data_saida', models.DateField(blank=True, null=True, verbose_name='Data Saída')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
        migrations.CreateModel(
            name='ItemProdutoCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Item Produto Compra',
                'verbose_name_plural': 'Itens Produto Compra',
            },
        ),
        migrations.CreateModel(
            name='ItemProdutoVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Item Produto Venda',
                'verbose_name_plural': 'Itens Produto Venda',
            },
        ),
        migrations.CreateModel(
            name='ItemServicoCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Item Serviço Compra',
                'verbose_name_plural': 'Itens Serviço Compra',
            },
        ),
        migrations.CreateModel(
            name='ItemServicoVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Item Serviço Venda',
                'verbose_name_plural': 'Itens Serviço Venda',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('ano', models.CharField(max_length=20, verbose_name='Ano')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelos', to='oficina.Marca')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelo',
            },
        ),
        migrations.CreateModel(
            name='PedidoCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('data_inicio', models.DateField(auto_now_add=True, verbose_name='Data Entrada')),
                ('data_termino', models.DateField(blank=True, null=True, verbose_name='Data Saída')),
                ('km', models.IntegerField(blank=True, null=True, verbose_name='KM')),
            ],
            options={
                'verbose_name': 'Pedido Compra',
                'verbose_name_plural': 'Pedidos Compra',
            },
        ),
        migrations.CreateModel(
            name='PedidoVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('data_inicio', models.DateField(auto_now_add=True, verbose_name='Data Entrada')),
                ('data_termino', models.DateField(blank=True, null=True, verbose_name='Data Saída')),
                ('km', models.IntegerField(blank=True, null=True, verbose_name='KM')),
            ],
            options={
                'verbose_name': 'Pedido Venda',
                'verbose_name_plural': 'Pedidos Venda',
            },
        ),
        migrations.CreateModel(
            name='PessoaVeiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('DN', 'Dono'), ('AT', 'Antigo')], max_length=2, verbose_name='Status')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('km', models.IntegerField(verbose_name='KM')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pessoa_veiculos', to='core.Pessoa')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacoes', models.TextField(verbose_name='Observações')),
                ('ano', models.CharField(max_length=20, verbose_name='Ano')),
                ('km', models.IntegerField(blank=True, null=True, verbose_name='KM')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veiculos', to='oficina.Cor')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veiculos', to='oficina.Modelo')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.AddField(
            model_name='pessoaveiculo',
            name='veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pessoa_veiculos', to='oficina.Veiculo'),
        ),
        migrations.AddField(
            model_name='pedidovenda',
            name='pessoa_veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos_venda', to='oficina.PessoaVeiculo'),
        ),
        migrations.AddField(
            model_name='pedidocompra',
            name='pessoa_veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos_compra', to='oficina.PessoaVeiculo'),
        ),
        migrations.AddField(
            model_name='itemservicovenda',
            name='pedido_venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_servico', to='oficina.PedidoVenda'),
        ),
        migrations.AddField(
            model_name='itemservicovenda',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_servico_venda', to='oficina.Servico'),
        ),
        migrations.AddField(
            model_name='itemservicocompra',
            name='pedido_compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_servico', to='oficina.PedidoCompra'),
        ),
        migrations.AddField(
            model_name='itemservicocompra',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_servico_compra', to='oficina.Servico'),
        ),
        migrations.AddField(
            model_name='itemprodutovenda',
            name='pedido_venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_produto', to='oficina.PedidoVenda'),
        ),
        migrations.AddField(
            model_name='itemprodutovenda',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_produto_venda', to='oficina.Produto'),
        ),
        migrations.AddField(
            model_name='itemprodutocompra',
            name='pedido_compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_produto', to='oficina.PedidoCompra'),
        ),
        migrations.AddField(
            model_name='itemprodutocompra',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_produto_compra', to='oficina.Produto'),
        ),
        migrations.AddField(
            model_name='faturarecebimento',
            name='pedido_venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faturas', to='oficina.PedidoVenda'),
        ),
        migrations.AddField(
            model_name='faturapagamento',
            name='pedidoCompra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faturas', to='oficina.PedidoCompra'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='produtos',
            field=models.ManyToManyField(related_name='categorias', to='oficina.Produto'),
        ),
        migrations.AddField(
            model_name='apontamento',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apontamentos', to='oficina.Funcionario'),
        ),
        migrations.AddField(
            model_name='apontamento',
            name='pedido_venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apontamentos', to='oficina.PedidoVenda'),
        ),
        migrations.AddField(
            model_name='apontamento',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apontamentos', to='oficina.Servico'),
        ),
        migrations.AlterUniqueTogether(
            name='pessoaveiculo',
            unique_together=set([('pessoa', 'veiculo')]),
        ),
    ]
