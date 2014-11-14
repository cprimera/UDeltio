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
			$scope.boards = []
			Restangular.all('me/favourites').getList().then(function (boards) {
				for (var i = 0; i < boards.length; i++) {
					var found = false;
					var idx = -1;
					for (var j = 0; j < $scope.boards.length; j++) {
						if ($scope.boards[j].id == boards[i].id) {
							found = true;
							idx = j;
							break;
						}
					}
					if (found) {
						$scope.boards[idx].favorite = true;
					} else {
						boards[i].favorite = true;
						boards[i].notify = false;
						$scope.boards.push(boards[i]);
					}
				}
			});


			Restangular.all('me/notify').getList().then(function (boards) {
				for (var i = 0; i < boards.length; i++) {
					var found = false;
					var idx = -1;
					for (var j = 0; j < $scope.boards.length; j++) {
						if ($scope.boards[j].id == boards[i].id) {
							found = true;
							idx = j;
							break;
						}
					}
					if (found) {
						$scope.boards[idx].notify = true;
					} else {
						boards[i].favorite = false;
						boards[i].notify = true;
						$scope.boards.push(boards[i]);
					}
				}
			});
		}
	};

	$scope.saveFavorite = function (board) {
		if (board.favorite) {
			Restangular.one('boards', board.id).customPOST(board.favorite, 'favourite');
		} else {
			Restangular.one('boards', board.id).customDELETE('favourite');
		}
	};

	$scope.saveNotify = function (board) {
		if (board.notify) {
			Restangular.one('boards', board.id).customPOST(board.notify, 'notify');
		} else {
			Restangular.one('boards', board.id).customDELETE('notify');
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

			$rootScope.authenticated = true;
			Restangular.one('me').get().then(function (user) {
				$rootScope.currentUser = user;
                $cookieStore.put('currentUser', user);
			});
		});
	};

	$scope.newBoard = {"name":"", "public":true};


	$scope.saveBoard = function() {
		Restangular.one('boards').customPOST($scope.newBoard).then(function(postedData) {
			$scope.newBoard = {"name":"", "public":true};
			$scope.boards.push(postedData);
			$("#createBoardModal").modal("toggle");
		});
	}

	$scope.newuser = {'username': '', 'read': false, 'write': false, 'admin': false};

	$scope.saveUser = function() {
		return Restangular.one('boards', $routeParams['id']).customPOST($scope.newuser, 'users').then(function(data) {
			$scope.users.push(data);
			$scope.newuser = {'username': '', 'read': false, 'write': false, 'admin': false};
		});
	};


	$scope.$on('logout', function(event) {
		$scope.boards = null;
	});

}]);