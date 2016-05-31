(function() {
    'use strict';
    angular.module('core')
    
    .controller('PessoaController', ['$stateParams', 'PessoaService','$scope', function($stateParams, PessoaService, $scope){
        $scope.pessoa = PessoaService.getNewEntity();
        
        var TIPO_PESSOA_FISICA = PessoaService.TIPO_PESSOA_FISICA;
        var TIPO_PESSOA_JURIDICA = PessoaService.TIPO_PESSOA_JURIDICA;
        
        $scope.tipos = [ TIPO_PESSOA_FISICA, TIPO_PESSOA_JURIDICA ];

        if($stateParams.id !== null){
            PessoaService.findById($stateParams.id).then(function(data){
                $scope.pessoa = data;
            });
        }

        $scope.edit = {};

        $scope.submit = function(){
            if( $scope.pessoa.id === null ){
                console.log('Inserindo novo registro ', $scope.pessoa)
                PessoaService.create($scope.pessoa)
                .then(function(data){
                    console.log(data);
                });
            } else {
                console.log('Atualizando novo registro ', $scope.pessoa)
                PessoaService.update($scope.pessoa, $scope.pessoa.id)
                .then(function(data){
                    console.log(data);
                });
            }
            $scope.reset();
        };
        $scope.reset = function(){
            $scope.pessoa = PessoaService.getNewEntity();
            $scope.formulario.$setPristine();
        };

        $scope.adicionarContato = function(index){
            $scope.pessoa.contatos.push( PessoaService.getNewContato() );
            $scope.edit[index] = true;
        };

        $scope.removerContato = function(index){
            $scope.pessoa.contatos.splice(index,1);
            delete $scope.edit[index];
        };
        $scope.editarContato = function(index){
            if($scope.edit[index] !== undefined){
                delete $scope.edit[index];
            }else{
                $scope.edit[index] = true;
            }
        };
    }])

    .controller('ListPessoaController', ['PessoaService','$scope', function(PessoaService, $scope){
        $scope.pessoas = [];
        var page = 1;
        var limit = 10;
        $scope.TIPO_PESSOA_FISICA = PessoaService.TIPO_PESSOA_FISICA;
        $scope.TIPO_PESSOA_JURIDICA = PessoaService.TIPO_PESSOA_JURIDICA;
        PessoaService.fetchAll(page, limit).then(function(data){
            $scope.pessoas = data.results;
        });
    }])
    ;

})();