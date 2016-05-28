(function() {
    'use strict';
    angular.module("conta")
    .config(['$interpolateProvider', '$httpProvider',function($interpolateProvider, $httpProvider){
        $interpolateProvider.startSymbol('({').endSymbol('})');
        $httpProvider.defaults.useXDomain = true;
        delete $httpProvider.defaults.headers.common['X-Requested-With'];
    }]);

 })();