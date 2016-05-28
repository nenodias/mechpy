(function() {
    'use strict';
    angular.module('conta')
    .config( ['$stateProvider','$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
      $stateProvider
      .state('home', {
        url: '/',
        params:{modulo:null, nome:null, id:null},
        templateUrl: 'static/app/conta/views/home.html',
        controller: 'HomeController',
        acesso:{
          requerido: true,
        }
      })
      .state('dinamico', {
        url: '/{modulo}/{nome}/{id:[/d+]}',
        params:{modulo:null, nome:null, id:null},
        templateUrl: 'static/app/conta/views/home.html',
        controller: 'HomeController',
        acesso:{
          requerido: true,
        }
      })
      .state('login', {
        url: '/login',
        templateUrl: 'static/app/conta/views/login-form.html',
        controller: 'LoginController',
      });
      $urlRouterProvider.otherwise('/');
    }])
    .run(['$rootScope', '$state', 'LoginService', function ($rootScope, $state, LoginService) {
        $rootScope.year = new Date().getFullYear();
        $rootScope.$on('$stateChangeStart', function (event, toState, toParams, fromState, fromParams) {
          $rootScope.current = toState;
            if ( ( (toState.acesso !== undefined  && toState.acesso.requerido === true ) && !LoginService.permissao() ) ) {
                console.log('DENY');
                event.preventDefault();
                $state.go('login');
            }
        });
    }]);

})();