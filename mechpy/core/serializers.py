from rest_framework import serializers
from .models import Pais, Estado, Cidade, Contato, Pessoa, PessoaFisica, PessoaJuridica, Endereco

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('id','nome','sigla')


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ('id','nome','sigla', 'pais')

class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
        fields = ('id','nome','codigo_ibge', 'estado')


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ('id','nome','email', 'telefone')

class EnderecoSerializer(serializers.ModelSerializer):

    cidade = CidadeSerializer()

    class Meta:
        model = Endereco
        fields = (
            'id',
            'nome',
            'numero',
            'rua',
            'bairro',
            'cep',
            'cidade',
            'pessoa'
        )

class PessoaJuridicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaJuridica
        fields = (
            'cnpj',
            'razao_social', 
            'nome_fantasia',
            'descricao',
            'inscricao_estadual',
            'inscricao_municipal'
        )

class PessoaFisicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaFisica
        fields = ('rg','cpf')

class PessoaSerializer(serializers.ModelSerializer):

    pessoa_juridica = PessoaJuridicaSerializer(required=False)
    pessoa_fisica = PessoaFisicaSerializer(required=False)
    contatos = ContatoSerializer(many=True, required=False)
    enderecos = EnderecoSerializer(many=True, required=False)

    def get_dicionario_relacoes(self, validated_data):
        relacionamentos = ['pessoa_juridica', 'pessoa_fisica', 'contatos', 'enderecos']
        dicionarios = {}
        for relacao in relacionamentos:
            try:
                dicionarios[relacao] = None
                dicionarios[relacao] = validated_data.pop(relacao)
            except:
                pass
        return dicionarios

    def create(self, validated_data):
        dicionarios = self.get_dicionario_relacoes(validated_data)
        pessoa = Pessoa.objects.create(**validated_data)
        if dicionarios['pessoa_juridica']:
            pessoa_juridica = PessoaJuridica.objects.create(**dicionarios['pessoa_juridica'])
            pessoa.pessoa_juridica = pessoa_juridica
            pessoa.tipo = Pessoa.TIPO_PESSOA_JURIDICA
        if dicionarios['pessoa_fisica']:
            pessoa_fisica = PessoaFisica.objects.create(**dicionarios['pessoa_fisica'])
            pessoa.pessoa_fisica = pessoa_fisica
            pessoa.tipo = Pessoa.TIPO_PESSOA_FISICA
        return pessoa

    def update(self, instance, validated_data):
        dicionarios = self.get_dicionario_relacoes(validated_data)
        pessoa = super(PessoaSerializer, self).update(instance, validated_data)
        if dicionarios['pessoa_juridica']:
            try:
                pessoa.pessoa_fisica.delete()
            except:
                pass
            pessoa_juridica = PessoaJuridica.objects.create(**dicionarios['pessoa_juridica'])
            pessoa.pessoa_juridica = pessoa_juridica
            pessoa.tipo = Pessoa.TIPO_PESSOA_JURIDICA
        if dicionarios['pessoa_fisica']:
            try:
                pessoa.pessoa_juridica.delete()
            except:
                pass
            pessoa_fisica = PessoaFisica.objects.create(**dicionarios['pessoa_fisica'])
            pessoa.pessoa_fisica = pessoa_fisica
            pessoa.tipo = Pessoa.TIPO_PESSOA_FISICA
        return pessoa

    class Meta:
        model = Pessoa
        fields = (
            'id',
            'nome',
            'observacao',
            'telefone',
            'celular',
            'email',
            'tipo',
            'pessoa_juridica',
            'pessoa_fisica',
            'contatos',
            'enderecos'
        )