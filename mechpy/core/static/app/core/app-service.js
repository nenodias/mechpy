(function() {
    'use strict';
    angular.module('conta')
    .factory('PessoaService', ['$http','$rootScope', '$state', '$stateParams', '$q',
    function($http,$rootScope, $state, $stateParams, $q) {
        var raiz = '';
        var api = '/api/pessoas/';
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
            fetchAll: function(){
                return $http.get(raiz + api)
                .then(
                    trataResposta,
                    trataErro('Erro ao carregar registros')
                );
            },
            create: function(entity){
                return $http.post(raiz + api, entity)
                .then(
                    trataResposta,
                    trataErro('Erro ao inserir registro')
                );
            },
            update: function(entity, id){
                return $http.put(raiz + api + id, entity)
                .then(
                    trataResposta,
                    trataErro('Erro ao atualizar registro')
                );
            },
            delete: function(id){
                return $http.delete(raiz + api + id)
                .then(
                    trataResposta,
                    trataErro('Erro ao excluir registro')
                );
            }
        };
    }]);

})();