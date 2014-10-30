/*global $:false jQUery:false */
'use strict';

// Declare app level module which depends on views, and components
var uDeltio = angular.module('UDeltio', [
    'ngRoute',
    'restangular',
    'MainCtrl',
    'BoardCtrl',
    'ProfileCtrl',
    'MenuCtrl',
    'ngCookies'
]);

uDeltio.config(['$routeProvider', function($routeProvider, $scope) {
    $routeProvider.when('/profile', {
        templateUrl: 'static/templates/profile.html',
        controller: 'ProfileCtrl'
    });
    $routeProvider.when('/board/:id', {
        templateUrl: 'static/templates/board.html',
        controller: 'BoardCtrl'
    });
    $routeProvider.when('/board_settings/:param', {
        templateUrl: 'static/templates/board_settings.html',
        controller: 'BoardSettingsCtrl'
    });
    $routeProvider.when('/create_board', {
        templateUrl: 'static/templates/board_settings.html',
        controller: 'CreateBoardCtrl'
    });
    $routeProvider.otherwise({redirectTo: '/profile'});
}]);

uDeltio.run(function run($http, $cookieStore) {

    var token = $cookieStore.get('token');
    $http.defaults.headers.common['Authorization']  = 'Bearer ' + token;

});

uDeltio.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl('http://udeltio.com/api/v1.0');
});
