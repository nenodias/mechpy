(function() {
    'use strict';
    angular.module("conta")
    .config(['$interpolateProvider', '$httpProvider',function($interpolateProvider, $httpProvider){
        $interpolateProvider.startSymbol('({').endSymbol('})');
        $httpProvider.defaults.useXDomain = true;
        /*
        $http.defaults.headers.common['Content-Type'] = 'application/json';
        $http.defaults.headers.common['Accept'] = 'application/json';
        */
        delete $httpProvider.defaults.headers.common['X-Requested-With'];
    }]);

 })();