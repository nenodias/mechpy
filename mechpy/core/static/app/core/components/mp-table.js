(function(){
    'use strict';
    angular.module("core")
    .component('mpTable', {
        transclude: true,
        controller: function() {
            console.log('teste');
        },
        templateUrl: 'static/app/core/components/views/mp-table.html',
    })
    ;
})();