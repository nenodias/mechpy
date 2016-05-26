# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('codigo_ibge', models.CharField(null=True, verbose_name='Código IBGE', blank=True, max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Cidades',
                'verbose_name': 'Cidade',
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=20)),
                ('email', models.EmailField(null=True, verbose_name='Email', blank=True, max_length=254)),
                ('telefone', models.CharField(verbose_name='Telefone', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Contatos',
                'verbose_name': 'Contato',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('numero', models.CharField(verbose_name='Número', max_length=50)),
                ('rua', models.CharField(verbose_name='Rua', max_length=100)),
                ('bairro', models.CharField(verbose_name='Bairro', max_length=100)),
                ('cep', models.CharField(verbose_name='Cep', max_length=20)),
                ('cidade', models.OneToOneField(verbose_name='Cidade', to='core.Cidade')),
            ],
            options={
                'verbose_name_plural': 'Endereços',
                'verbose_name': 'Endereço',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('sigla', models.CharField(verbose_name='Sigla', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Estados',
                'verbose_name': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('sigla', models.CharField(verbose_name='Sigla', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Países',
                'verbose_name': 'País',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=200)),
                ('observacao', models.TextField(verbose_name='Observação', blank=True, null=True)),
                ('telefone', models.CharField(verbose_name='Telefone', max_length=20)),
                ('celular', models.CharField(verbose_name='Celular', max_length=20)),
                ('email', models.EmailField(verbose_name='Email', max_length=254)),
                ('tipo', models.CharField(verbose_name='Tipo', choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Pessoas',
                'verbose_name': 'Pessoa',
            },
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('rg', models.CharField(verbose_name='RG', max_length=20)),
                ('cpf', models.IntegerField(verbose_name='CPF', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Pessoas Físicas',
                'verbose_name': 'Pessoa Física',
            },
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('cnpj', models.IntegerField(verbose_name='CNPJ', blank=True, null=True)),
                ('razao_social', models.CharField(verbose_name='Razão Social', max_length=200)),
                ('nome_fantasia', models.CharField(verbose_name='Nome Fantasia', max_length=200)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=200)),
                ('inscricao_estadual', models.CharField(verbose_name='Inscrição Estadual', max_length=30)),
                ('inscricao_municipal', models.CharField(verbose_name='Inscrição Municipal', max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Pessoas Jurídicas',
                'verbose_name': 'Pessoa Jurídica',
            },
        ),
        migrations.AddField(
            model_name='pessoa',
            name='pessoa_fisica',
            field=models.OneToOneField(verbose_name='Pessoa Física', blank=True, null=True, to='core.PessoaFisica'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='pessoa_juridica',
            field=models.OneToOneField(verbose_name='Pessoa Jurídica', blank=True, null=True, to='core.PessoaJuridica'),
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(related_name='estados', to='core.Pais'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='pessoa',
            field=models.ForeignKey(related_name='enderecos', to='core.Pessoa'),
        ),
        migrations.AddField(
            model_name='contato',
            name='pessoa',
            field=models.ForeignKey(related_name='contatos', to='core.Pessoa'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(related_name='cidades', to='core.Estado'),
        ),
    ]
