(function() {
    'use strict';
    angular.module('conta')
    .factory('LoginService', ['$rootScope', '$http', '$cookies', '$location', '$route',
    function($rootScope, $http, $cookies, $location, $route) {
        var servico = {};

        servico.logoff = function(){
          $rootScope.user = {'token':null,'username':null,'email':null,'name':null };
        };

        servico.logon = function(username, password){
          $http.post('/api/token/',{'username':username, 'password':password})
          .then(function successCallback(response) {
            console.log(response);
              var token = response.data.token;
              var config = {
                headers:  {
                  'Authorization': 'Token '+token,
                  'Content-type': 'application/json',
                  'Accept': 'application/json'
                }
              };
              $http.get('/api/users/'+username+'/', config).then(function(response){
                var d = response.data;
                $rootScope.user = {'token':token,'username':d.username,'email':d.email, 'name':d.name };
                $cookies.put('user',JSON.stringify( $rootScope.user ) );
                $location.path('/home');
              });
          }, function errorCallback(response) {
              //FAULT
              servico.logoff();
          });
        };

        servico.permissao = function(){
             $location.path();
             var permissao_necessaria = false;
             try{
                permissao_necessaria = $rootScope.current.acesso.requerido;
              }catch(exx){
                
              }
              if(permissao_necessaria){
                if ($cookies.get('user') !== undefined ){
                  //console.log('Cookie ' + $cookies.get('user'));
                  $rootScope.user = JSON.parse( $cookies.get('user') );
                  //console.log('Value ' +$rootScope.user);
                  //console.log('Ok  autenticacao');
                  return true;
                }else{
                  //console.log('Falha de autenticacao');
                  return false;
                }
              }else{
                return true;
              }
              return false;
         };
         return servico;
    }]);

 })();