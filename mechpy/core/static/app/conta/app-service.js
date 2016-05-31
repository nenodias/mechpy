(function() {
    'use strict';
    angular.module('conta')
    .factory('LoginService', ['$rootScope', '$http', '$cookies', '$state', '$stateParams', '$q',
    function($rootScope, $http, $cookies, $state, $stateParams, $q) {
        var servico = {};

        servico.logoff = function(){
          $cookies.remove('user');
          try{
            $rootScope.user = {'token':null,'username':null,'email':null,'name':null };
          }catch(err){}
          $state.go('login');
        };

        servico.getConfig = function(token){
          var config = {
            headers:  {
              'Authorization': 'Token '+token,
              'Content-type': 'application/json',
              'Accept': 'application/json'
            }
          };
          return config;
        };

        servico.logon = function(username, password){
          var d1 = $q.defer();
          $http.post('/api/token/',{'username':username, 'password':password})
          .then(function successCallback(response) {
              var token = response.data.token;
              var config = servico.getConfig(token);
              $rootScope.config = config;
              $http.get('/api/users/'+username+'/', config).then(function(response){
                var d = response.data;
                $rootScope.user = {'token':token,'username':d.username,'email':d.email, 'name':d.name };
                $cookies.put('user',JSON.stringify( $rootScope.user ) );
                $state.go('home');
                d1.resolve();
              });
          }, function errorCallback(response) {
              //FAULT
              servico.logoff();
              d1.resolve(false);
          });
          return d1.promise;
        };

        servico.permissao = function(){
             var permissao_necessaria = false;
             try{
                permissao_necessaria = $rootScope.current.acesso.requerido;
              }catch(exx){
                
              }
              console.log($cookies.get('user'));
              if(permissao_necessaria){
                if ($cookies.get('user') !== undefined ){
                  //console.log('Cookie ' + $cookies.get('user'));
                  $rootScope.user = JSON.parse( $cookies.get('user') );
                  $rootScope.config = servico.getConfig($rootScope.user.token);
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