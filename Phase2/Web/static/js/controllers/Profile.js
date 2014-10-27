'use strict';

var ProfileCtrl = angular.module('ProfileCtrl', ['restangular']);

ProfileCtrl.controller('ProfileCtrl', ['$scope', 'Restangular', function($scope, Restangular) {
    $scope.cname = "profile";

    Restangular.all('boards').getList().then(function(boards) {
        $scope.boards = boards;
    });

}]);

