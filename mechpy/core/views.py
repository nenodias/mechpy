from django.shortcuts import render
from rest_framework import viewsets

from .models import Pais, Estado, Cidade, Contato, Pessoa, PessoaFisica, PessoaJuridica, Endereco
from .serializers import PaisSerializer, EstadoSerializer, CidadeSerializer, PessoaSerializer

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.order_by('id')
    serializer_class = PaisSerializer
    search_fields = ('nome', 'sigla')

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.order_by('id')
    serializer_class = EstadoSerializer
    search_fields = ('nome', 'sigla')

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.order_by('id')
    serializer_class = CidadeSerializer
    search_fields = ('nome', 'codigo_ibge')

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.order_by('id')
    serializer_class = PessoaSerializer
    search_fields = ('nome', 'email', 'tipo', 'observacao', 'pessoa_juridica__cnpj', 'pessoa_fisica__cpf')