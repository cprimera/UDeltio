'use strict';

var ProfileCtrl = angular.module('ProfileCtrl', ['restangular', 'ngCookies']);

ProfileCtrl.controller('ProfileCtrl', ['$scope', '$rootScope', 'Restangular', '$cookieStore', '$http', function($scope, $rootScope, Restangular, $cookieStore, $http) {
    $scope.cname = "profile";
    $scope.username = null;
    $scope.password = null;

    $scope.loggedIn = function() {
        return $cookieStore.get('token') != null;
    }

    var getBoards = function() {
        if ($scope.loggedIn()) {
            Restangular.all('boards').getList().then(function (boards) {
                $scope.boards = boards;
            });
        }
    };

    getBoards();

    $scope.login = function() {
        var auth = Restangular.oneUrl('auth', 'http://udeltio.com/oauth2').customPOST({
            "client_id": "***REMOVED***",
            "client_secret": "***REMOVED***",
            "grant_type": "password",
            "username": $scope.username,
            "password": $scope.password
        },
        "access_token", {}, {}).then(function(response){
                $cookieStore.put('token', response.access_token);
                $http.defaults.headers.common['Authorization']  = 'Bearer ' + response.access_token;
                getBoards();
            });
    };

    $scope.$on('logout', function(event) {
        $scope.boards = null;
    });

}]);

