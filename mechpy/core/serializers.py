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
        extra_kwargs = {'id': {'read_only': False, 'required':False, 'allow_null':True}}

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

    def insert_or_update(self, pessoa, dicionarios):
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
        if dicionarios['contatos']:
            pk_novos = []
            for contato_data in dicionarios['contatos']:
                if 'id' in contato_data.keys():
                    pk = contato_data.pop('id')
                    contato = Contato(pessoa=pessoa,**contato_data)
                    contato.id = pk
                    contato.save()
                else:
                    contato = Contato.objects.create(pessoa=pessoa,**contato_data)
                pk_novos.append(contato.pk)
            if pk_novos:
                contatos_a_excluir = Contato.objects.filter(pessoa=pessoa).exclude(id__in=pk_novos)
                if contatos_a_excluir:
                    for contato_deletar in contatos_a_excluir:
                        contato_deletar.delete()
        return pessoa

    def create(self, validated_data):
        dicionarios = self.get_dicionario_relacoes(validated_data)
        pessoa = Pessoa.objects.create(**validated_data)
        pessoa = self.insert_or_update(pessoa, dicionarios)
        return pessoa

    def update(self, instance, validated_data):
        dicionarios = self.get_dicionario_relacoes(validated_data)
        pessoa = super(PessoaSerializer, self).update(instance, validated_data)
        pessoa = self.insert_or_update(pessoa, dicionarios)
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