'use strict';

var MenuCtrl = angular.module('MenuCtrl', ['ngCookies']);

MenuCtrl.controller('MenuCtrl', ['$scope', '$rootScope', '$cookieStore', '$location', function($scope, $rootScope, $cookieStore, $location) {

    $rootScope.currentUser = $cookieStore.get('currentUser');

    $scope.searchStr = "";

    $scope.loggedIn = function() {
        return $cookieStore.get('token') != null;
    }

    $scope.logOut = function() {
        $cookieStore.remove('token');
        $rootScope.$broadcast('logout');
        $location.path( "/profile" );
    }

    if(!$scope.loggedIn()) {
        $location.path("/profile");
    }

    $scope.search = function() {
        console.log($scope.searchStr);
        $rootScope.$broadcast('search', {'term': $scope.searchStr});
    }
}]);
