(function() {
    'use strict';
    angular.module('conta')
    .factory('PessoaService', ['$http','$rootScope', '$state', '$stateParams', '$q',
    function($http,$rootScope, $state, $stateParams, $q) {
        var raiz = '';
        var api = '/api/pessoas/';
        var sep = '/';
        var config = $rootScope.config;

        var TIPO_PESSOA_FISICA = { id: 'PF', nome: 'Pessoa Física' };
        var TIPO_PESSOA_JURIDICA = { id: 'PJ', nome: 'Pessoa Jurídica' };

        var trataResposta = function(response){
            return response.data;
        };
        var trataErro = function(mensagem){
            var retorno = function(errResponse){
                console.error(mensagem);
                return $q.reject(errResponse);
            };
            return retorno; 
        };

        var tratativaTipoPessoa = function(entity){
            if(entity.tipo === TIPO_PESSOA_FISICA.id){
                entity.pessoa_juridica = {};
                delete entity.pessoa_juridica;
            }else if(entity.tipo === TIPO_PESSOA_JURIDICA.id){
                entity.pessoa_fisica = {};
                delete entity.pessoa_fisica;
            }
            return entity;
        };

        return {
            TIPO_PESSOA_FISICA: TIPO_PESSOA_FISICA,
            TIPO_PESSOA_JURIDICA: TIPO_PESSOA_JURIDICA,
            getNewEntity: function (){
                return {
                    "id":null,
                    "nome":null,
                    "tipo":null,
                    "contatos" :[],
                    "enderecos":[],
                    "pessoa_fisica":{},
                    "pessoa_juridica":{}
                };
            },
            getNewContato: function (){
                return {
                    "nome" :null,
                    "email":null,
                    "telefone":null,
                };
            },
            findById: function(id){
                var filtros = '';
                return $http.get(raiz + api + id + sep, config)
                .then(
                    function(response){
                        var entity = response.data;
                        if(entity.tipo === TIPO_PESSOA_FISICA.id){
                            entity.pessoa_juridica = {};
                        }else if(entity.tipo === TIPO_PESSOA_JURIDICA.id){
                            entity.pessoa_fisica = {};
                        }
                        return response.data;
                    },
                    trataErro('Erro ao carregar registros')
                );
            },
            fetchAll: function(page, limit){
                var filtros = '';
                if(page !== undefined && limit !== undefined){
                    filtros = '?page='+page+'&limit='+limit;
                }
                return $http.get(raiz + api + filtros, config)
                .then(
                    function(response){
                        return response;
                    },
                    trataErro('Erro ao carregar registros')
                );
            },
            create: function(entity){
                entity = tratativaTipoPessoa(entity);
                return $http.post(raiz + api, entity, config)
                .then(
                    trataResposta,
                    trataErro('Erro ao inserir registro')
                );
            },
            update: function(entity, id){
                entity = tratativaTipoPessoa(entity);
                return $http.put(raiz + api + id + sep, entity, config)
                .then(
                    trataResposta,
                    trataErro('Erro ao atualizar registro')
                );
            },
            delete: function(id){
                return $http.delete(raiz + api + id + sep, config)
                .then(
                    trataResposta,
                    trataErro('Erro ao excluir registro')
                );
            }
        };
    }]);

})();