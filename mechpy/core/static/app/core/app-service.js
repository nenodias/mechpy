(function() {
    'use strict';
    angular.module('conta')
    .factory('PessoaService', ['$http','$rootScope', '$state', '$stateParams', '$q',
    function($http,$rootScope, $state, $stateParams, $q) {
        var raiz = '';
        var api = '/api/pessoas/';
        var sep = '/';
        var config = {
            headers:  {
                'Authorization': 'Token '+$rootScope.user.token,
                'Content-Type':'application/json; charset=utf-8',
                'Accept': 'application/json; charset=utf-8'
            }
        };

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
        return {
            findById: function(id){
                var filtros = '';
                return $http.get(raiz + api + id + sep, config)
                .then(
                    trataResposta,
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
                    trataResposta,
                    trataErro('Erro ao carregar registros')
                );
            },
            create: function(entity){
                return $http.post(raiz + api, entity, config)
                .then(
                    trataResposta,
                    trataErro('Erro ao inserir registro')
                );
            },
            update: function(entity, id){
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