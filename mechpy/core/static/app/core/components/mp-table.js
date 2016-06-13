(function(){
    'use strict';
    angular.module("core")
    .component('mpTable', {
        transclude: true,
        bindings: {
            headers: '=',
            metadata: '=',
            service: '='
        },
        controller: function($scope) {
            var self = this;
            
            $scope.headers = self.headers;
            $scope.metadata = self.metadata;

            $scope.dados = [];
            $scope.page = 1;
            $scope.limit = 10;
            $scope.count = 0;
            $scope.current = 0;

            self.service.fetchAll($scope.page, $scope.limit).then(function(data){
                $scope.current = ($scope.page * $scope.limit) - $scope.limit + data.results.length;
                $scope.count = data.count;
                $scope.dados = data.results;
            });
        },
        templateUrl: 'static/app/core/components/views/mp-table.html',
    })
    ;
})();