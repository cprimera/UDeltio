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
    //RestangularProvider.setBaseUrl('http://private-df2e0-udeltio.apiary-mock.com/api/v1.0');

    var token = '7a5535ed99be264884fb41287b0a925a20f39984';

    RestangularProvider.setBaseUrl('http://udeltio.com/api/v1.0');
    RestangularProvider.addFullRequestInterceptor(function(element, operation, route, url, headers, params) {
        return {
            element: element,
            params: params,
            headers: _.extend(headers, {Authorization: 'Bearer ' + token})
        };
    });

});
