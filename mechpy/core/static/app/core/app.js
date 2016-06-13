(function() {
    'use strict';
    angular.module('core',[])
    .filter('safe', ['$sce', function($sce){
        return function(text) {
            return $sce.trustAsHtml(text);
        };
    }])
    ;
 })();