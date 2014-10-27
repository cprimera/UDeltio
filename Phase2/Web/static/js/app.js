'use strict';

// Declare app level module which depends on views, and components
var uDeltio = angular.module('UDeltio', [
    'ngRoute',
    'restangular',
    'MainCtrl',
    'BoardCtrl',
    'ProfileCtrl',
    'MenuCtrl'
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

uDeltio.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl('http://private-72330-***REMOVED***.apiary-mock.com');
})


