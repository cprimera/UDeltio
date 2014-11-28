'use strict';

var MainCtrl = angular.module('MainCtrl', []);

MainCtrl.controller('MainCtrl', ['$scope', '$rootScope', '$location', function($scope, $rootScope, $location) {
		$scope.menu_template = 'static/templates/menu.html';
		$scope.submenu_template = 'static/templates/submenu.html';
		$rootScope.authenticated = false;
		
		$scope.go = function (path) {
			var param = $location.path().split("/")[2]||"";
			if (param !== "undefined") {
				$location.path(path + "/" + param);
			} else {
				$location.path(path);
			}
		};

		$scope.$on('logout', function(event) {
			$rootScope.authenticated = false;
		});
	}])	;