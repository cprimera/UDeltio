'use strict';

var BoardCtrl = angular.module('BoardCtrl', ['restangular']);


BoardCtrl.controller('BoardCtrl', ['$scope', 'Restangular', '$routeParams', function($scope, Restangular, $routeParams) {
    $scope.cname = "board";
    Restangular.one('boards', $routeParams['id']).get().then(function (board) {
        $scope.board = board;
    });

    Restangular.one('boards', $routeParams['id']).getList('posts').then(function (posts) {
        $scope.posts = posts;
    });
}])


BoardCtrl.controller('BoardSettingsCtrl', ['$scope', function($scope) {
    $scope.cname = "board_settings";
}])

BoardCtrl.controller('CreateBoardCtrl', ['$scope', function($scope) {
    $scope.cname = "create_board";
}])