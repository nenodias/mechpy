(function() {
    'use strict';
    angular.module('conta')
    .controller('HomeController', ['$scope',function($scope){
        var self = this;
        $scope.item1 = true;
        $scope.item2 = true;
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