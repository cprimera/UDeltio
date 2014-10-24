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
	  $routeProvider.when('/create_board', {
	    templateUrl: 'static/templates/board_settings.html',
	    controller: 'CreateBoardCtrl',
	  });
	  $routeProvider.otherwise({redirectTo: '/profile'});
	}])


	.controller('MainCtrl', ['$scope', '$location', function($scope, $location) {
		$scope.menu_template = 'static/templates/menu.html';
		$scope.submenu_template = 'static/templates/submenu.html';

		$scope.go = function (path) {
		  var param = $location.path().split("/")[2]||"";
		  if (param !== "undefined") {
		  	$location.path(path + "/" + param);
		  } else {
		  	$location.path(path);
		  }
		};
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

	.controller('CreateBoardCtrl', ['$scope', function($scope) {
		$scope.cname = "create_board";
	}])

	.controller('MenuCtrl', ['$scope', function($scope) {
	}]);



