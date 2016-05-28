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
            'id',
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
        fields = ('id','rg','cpf')

class PessoaSerializer(serializers.ModelSerializer):

    pessoa_juridica = PessoaJuridicaSerializer()
    pessoa_fisica = PessoaFisicaSerializer()
    contatos = ContatoSerializer()
    enderecos = EnderecoSerializer()

    def create(self, validated_data):
        pessoa = Pessoa.objects.create(**validated_data)
        try:
            pessoa_juridica_data = validated_data.pop('pessoa_juridica')
            PessoaJuridica.create(pessoa=pessoa, **pessoa_juridica_data)
            pessoa.tipo = Pessoa.TIPO_PESSOA_JURIDICA
        except:
            pass
        try:
            pessoa_fisica_data = validated_data.pop('pessoa_fisica')
            PessoaFisica.create(pessoa=pessoa, **pessoa_fisica_data)
            pessoa.tipo = Pessoa.TIPO_PESSOA_FISICA
        except:
            pass
        return pessoa

    def update(self, instance, validated_data):
        return super(PessoaSerializer, self).update(instance, validated_data)

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