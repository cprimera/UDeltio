'use strict';

var MenuCtrl = angular.module('MenuCtrl', ['ngCookies']);

MenuCtrl.controller('MenuCtrl', ['$scope', '$rootScope', '$cookieStore', function($scope, $rootScope, $cookieStore) {
    $scope.loggedIn = function() {
        return $cookieStore.get('token') != null;
    }

    $scope.logOut = function() {
        $cookieStore.remove('token');
        $rootScope.$broadcast('logout');
    }
}]);
