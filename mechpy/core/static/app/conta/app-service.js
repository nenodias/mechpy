(function() {
    'use strict';
    angular.module('conta')
    .value('user', {'token':null,'username':null,'email':null })
    .factory('LoginService', ['user', '$http', '$rootScope', '$cookieStore', '$location', '$route',
    function($http, $rootScope, $cookieStore, $location, $route) {
        var servico = {};

        servico.logoff = function(){
          user = {'token':null,'username':null,'email':null };
        };

        servico.logon = function(username, password){
          $http.post('/api/token/',{'username':username, 'password':password})
          .then(function successCallback(response) {
            console.log(response);
              $http.get('/api/users/',{'username':username, 'password':password})
              user = {'token':token,'username':null,'email':null }
              $location.path('/home');
          }, function errorCallback(response) {
              //FAULT
              servico.logoff();
          });
        };

         servico.permissao = function(){
             $rootScope.location_path = $location.path();
             var permissao_necessaria = false;
             $rootScope.logged = false;
             try{
               if ($cookieStore.get('globals') !== undefined && $cookieStore.get('globals').currentUser !== undefined){
                 $rootScope.globals = $cookieStore.get('globals');
               }
               permissao_necessaria = $route.current.acesso.requerido;
             }catch(exx){}
             if ( $rootScope.globals !== undefined && $rootScope.globals.currentUser !== undefined ){
                 $rootScope.logged = true;
                 console.log('Ok  autenticacao');
                 return true;
             }else if ( permissao_necessaria ) {
                 console.log('Falha de autenticacao');
                 return false;
             }
         };
         return servico;
    }]);

 })();