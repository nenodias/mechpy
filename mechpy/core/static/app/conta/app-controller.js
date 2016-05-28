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
        $scope.doLogin = function(){
            console.log('Tentou login');
            LoginService.logon($scope.username, $scope.password);
        };
    }])
    
    ;

})();