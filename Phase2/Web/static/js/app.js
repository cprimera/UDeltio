'use strict';

// Declare app level module which depends on views, and components
angular.module('UDeltio', ['ngRoute',])
	.config(['$routeProvider', function($routeProvider, $scope) {
	  $routeProvider.when('/profile', {
	    templateUrl: 'static/templates/profile.html',
	    controller: 'ProfileCtrl',
	  });
	  $routeProvider.when('/board/:param', {
	    templateUrl: 'static/templates/board.html',
	    controller: 'BoardCtrl',
	  });
	  $routeProvider.otherwise({redirectTo: '/profile'});
	}])


	.controller('MainCtrl', ['$scope', function($scope) {
		$scope.menu_template = 'static/templates/menu.html';
	}])	

	.controller('BoardCtrl', ['$scope', function($scope) {
	}])

	.controller('ProfileCtrl', ['$scope', function($scope) {
	}])

	.controller('MenuCtrl', ['$scope', function($scope) {
	}]);		
