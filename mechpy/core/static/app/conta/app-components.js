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
            controller: function(){
                var self = this;
                self.username = null;
                self.email = null;
            },
            controllerAs:'login'
        };
    })
    ;
})();