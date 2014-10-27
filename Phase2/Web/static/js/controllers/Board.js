'use strict';

var BoardCtrl = angular.module('BoardCtrl', ['restangular']);


BoardCtrl.controller('BoardCtrl', ['$scope', 'Restangular', '$routeParams', function($scope, Restangular, $routeParams) {
    $scope.cname = "board";
    $scope.doofus = "Doofus";
    Restangular.one('boards', $routeParams['id']).get().then(function (board) {
        $scope.board = board;
    });
    console.log("Board Controller running");
    console.log($scope.board);
    console.log($routeParams);
}])


BoardCtrl.controller('BoardSettingsCtrl', ['$scope', function($scope) {
    $scope.cname = "board_settings";
}])

BoardCtrl.controller('CreateBoardCtrl', ['$scope', function($scope) {
    $scope.cname = "create_board";
}])