(function() {
    'use strict';
    angular.module('core')
    
    .controller('PessoaController', ['$rootScope','$scope', function($rootScope, $scope){
        $scope.valor = "Meu valor";
        console.log('Pessoa Controller foi Chamado');
        console.log($rootScope);
    }])

    .controller('ListPessoaController', ['PessoaService','$scope', function(PessoaService, $scope){
        $scope.pessoas = [];
        PessoaService.fetchAll().then(function(data){
            console.log(data.results);
        });
    }])
    ;

})();