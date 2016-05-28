(function() {
    'use strict';
    angular.module('conta')
    .config( ['$routeProvider','$locationProvider', function($routeProvider, $locationProvider) {
        $locationProvider.html5Mode({
          enabled: true,
          requireBase: false
        }).hashPrefix('!');
        $routeProvider
        .when('/', {
           templateUrl : 'static/app/conta/views/home.html',
           controller     : 'HomeController',
           acesso: {
             requerido: true
           }
        })

        .when('/login', {
           templateUrl : 'static/app/conta/views/login-form.html',
           controller     : 'LoginController'
        })

        .otherwise ({ redirectTo: '/' });
    }])
    .run(['$rootScope', '$location', 'LoginService', function ($rootScope, $location, LoginService) {
        $rootScope.year = new Date().getFullYear();
        $rootScope.$on('$routeChangeStart', function(event, next, current) {
          $rootScope.current = next;
            if ( ( (next.acesso !== undefined  && next.acesso.requerido === true ) && !LoginService.permissao() ) ) {
                console.log('DENY');
                event.preventDefault();
                $location.path('/login');
            }
        });
    }]);

})();