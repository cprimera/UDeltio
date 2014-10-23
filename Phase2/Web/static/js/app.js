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
	  $routeProvider.when('/board_settings/:param', {
	    templateUrl: 'static/templates/board_settings.html',
	    controller: 'BoardSettingsCtrl',
	  });
	  $routeProvider.otherwise({redirectTo: '/profile'});
	}])


	.controller('MainCtrl', ['$scope', function($scope) {
		$scope.menu_template = 'static/templates/menu.html';
		$scope.submenu_template = 'static/templates/submenu.html';
	}])	

	.controller('BoardCtrl', ['$scope', function($scope) {
		$scope.cname = "board";
	}])

	.controller('ProfileCtrl', ['$scope', function($scope) {
		$scope.cname = "profile";
	}])

	.controller('BoardSettingsCtrl', ['$scope', function($scope) {
		$scope.cname = "board_settings";
	}])

	.controller('MenuCtrl', ['$scope', function($scope) {
	}]);



