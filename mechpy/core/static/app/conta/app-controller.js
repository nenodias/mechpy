(function() {
    'use strict';
    angular.module('conta')
    .controller('HomeController', ['$scope','$stateParams',function($scope, $stateParams){
        var modulo = $stateParams.modulo;
        var nome = $stateParams.nome;
        if(modulo !== null && nome !== null){
            $scope.template_name = 'static/app/' + modulo + '/views/' +nome + '.html';
        }
        if($stateParams.id !== null){
            $scope.entidadeId = $stateParams.id;
        }
        if($stateParams.alerts !== null){
            $scope.alerts = $stateParams.alerts;
            $stateParams.alerts = null;
        }
        $scope.item1 = true;
        $scope.item2 = true;
        
        $scope.closeAlert = function(index){
            $scope.alerts.splice(index, 1);
        };
    }])
    .controller('LoginController', ['LoginService', '$scope', function(LoginService, $scope){
        var self = this;
        $scope.username = null;
        $scope.password = null;
        $scope.alerts = [];
        $scope.closeAlert = function(index){
            $scope.alerts.splice(index, 1);
        };
        $scope.doLogin = function(){
            LoginService.logon($scope.username, $scope.password).then(function(data){
                if(!data){
                    $scope.alerts = [];
                    $scope.alerts.push({type:'alert',msg: "Ocorreu um erro ao efetuar Login!"});
                }
            });
        };
    }])
    
    ;

})();