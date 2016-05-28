(function() {
    'use strict';
    angular.module('core')
    .controller('PessoaController', ['$rootScope','$scope', function($rootScope, $scope){
        $scope.valor = "Meu valor";
        console.log('Pessoa Controller foi Chamado');
        console.log($rootScope);
    }])
    ;

})();