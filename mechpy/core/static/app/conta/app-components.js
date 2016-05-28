(function(){
    'use strict';
    angular.module("conta")
    .directive('menuEsquerdo', function(){
        return{
            restrict:'E',
            templateUrl:'static/app/conta/views/menu-esquerdo.html',
            controller: function(){
                //TODO
            },
            controllerAs:'menu'
        };
    })
    .directive('dadosPerfil', function(){
        return{
            restrict:'E',
            templateUrl:'static/app/conta/views/dados-perfil.html',
            controller: ['$rootScope', 'LoginService',function($rootScope, LoginService){
                var self = this;
                self.username = null;
                self.email = null;
                if($rootScope.user !== undefined){
                    self.username = $rootScope.user.username;
                    self.email = $rootScope.user.email;
                }
                self.logout = function(){
                    LoginService.logoff();
                    console.log('Logout');
                };
            }],
            controllerAs:'dados'
        };
    })
    ;
})();