(function() {
    'use strict';
    angular.module('core')
    
    .controller('PessoaController', ['$stateParams', 'PessoaService','$scope', function($stateParams, PessoaService, $scope){
        $scope.pessoa = {};
        var TIPO_PESSOA_FISICA = { id: 'PF', name: 'Pessoa Física' };
        var TIPO_PESSOA_JURIDICA = { id: 'PJ', name: 'Pessoa Jurídica' };
        $scope.tipos = [ TIPO_PESSOA_FISICA, TIPO_PESSOA_JURIDICA ];
        PessoaService.findById($stateParams.id).then(function(data){
            $scope.pessoa = data;
        });
    }])

    .controller('ListPessoaController', ['PessoaService','$scope', function(PessoaService, $scope){
        $scope.pessoas = [];
        var page = 1;
        var limit = 10;
        PessoaService.fetchAll(page, limit).then(function(data){
            $scope.pessoas = data.results;
        });
    }])
    ;

})();