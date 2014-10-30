'use strict';

var MenuCtrl = angular.module('MenuCtrl', ['ngCookies']);

MenuCtrl.controller('MenuCtrl', ['$scope', '$cookieStore', function($scope, $cookieStore) {
    $scope.loggedIn = function() {
        return $cookieStore.get('token') != null;
    }

    $scope.logOut = function() {
        $cookieStore.remove('token');
    }
}]);
