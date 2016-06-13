(function() {
    'use strict';
    angular.module('core')
    
    .controller('PessoaController', ['$state','$stateParams', 'PessoaService','$scope', function($state, $stateParams, PessoaService, $scope){
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
                    var alerts = [];
                    alerts.push({type:'success',msg: "Registro inserido com sucesso!"});
                    $state.go('dinamico',{modulo:'core', nome:'pessoa-list', id:null, alerts: alerts });
                });
            } else {
                console.log('Atualizando novo registro ', $scope.pessoa)
                PessoaService.update($scope.pessoa, $scope.pessoa.id)
                .then(function(data){
                    console.log(data);
                    var alerts = [];
                    alerts.push({type:'success',msg: "Registro atualizado com sucesso!"});
                    $state.go('dinamico',{modulo:'core', nome:'pessoa-list', id:null, alerts: alerts });
                });
            }
        };
        $scope.reset = function(){
            $scope.pessoa = PessoaService.getNewEntity();
            $scope.formulario.$setPristine();
        };

        $scope.adicionarContato = function(){
            var index = $scope.pessoa.contatos.length;
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
        $scope.page = 1;
        $scope.limit = 10;
        $scope.count = 0;
        $scope.current = 0;

        $scope.TIPO_PESSOA_FISICA = PessoaService.TIPO_PESSOA_FISICA;
        $scope.TIPO_PESSOA_JURIDICA = PessoaService.TIPO_PESSOA_JURIDICA;

        $scope.headers = [
            { body:'Id'},
            { attr:'width="200"',body:'Nome'},
            { body:'Telefone'},
            { attr:'width="150"',body:'Celular'},
            { attr:'width="150"',body:'Email'},
            { attr:'width="150"',body:'Tipo'},
            {}
        ];
        
        $scope.metadata = [
            { modelo:'id'},
            { modelo:'nome'},
            { modelo:'telefone'},
            { modelo:'celular'},
            { modelo:'email'},
            { modelo:'tipo'},
            { 
                html: "<a> botão</a>"
            }
        ];
        $scope.pessoaService = PessoaService;
        PessoaService.fetchAll($scope.page, $scope.limit).then(function(data){
            $scope.current = ($scope.page * $scope.limit) - $scope.limit + data.results.length;
            $scope.count = data.count;
            $scope.pessoas = data.results;
        });
    }])
    ;

})();