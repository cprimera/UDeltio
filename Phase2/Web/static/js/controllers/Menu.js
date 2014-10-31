'use strict';

var MenuCtrl = angular.module('MenuCtrl', ['ngCookies']);

MenuCtrl.controller('MenuCtrl', ['$scope', '$rootScope', '$cookieStore', '$location', function($scope, $rootScope, $cookieStore, $location) {
    $scope.loggedIn = function() {
        return $cookieStore.get('token') != null;
    }

    $scope.logOut = function() {
        $cookieStore.remove('token');
        $rootScope.$broadcast('logout');
        $location.path( "/profile" );
    }

    if(!loggedIn()) {
        $location.path("/profile");
    }
}]);
