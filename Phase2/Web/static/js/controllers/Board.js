'use strict';

var BoardCtrl = angular.module('BoardCtrl', ['restangular']);


BoardCtrl.controller('BoardCtrl', ['$scope', 'Restangular', '$routeParams', function($scope, Restangular, $routeParams) {
	$scope.cname = "board";
	Restangular.one('boards', $routeParams['id']).get().then(function (board) {
		$scope.board = board;
	});

	Restangular.one('boards', $routeParams['id']).getList('posts').then(function (posts) {
		$scope.posts = posts;
	});

	Restangular.one('boards', $routeParams['id']).getList('users').then(function (users) {
		$scope.users = users;
	});
	
	$scope.toggle = function(user, item) {
		user[item] = !user[item];
	}

	$scope.saveBoard = function() {
		$scope.board.put().then(function (data) {
			for(var i = 0; i < $scope.users.length; i++) {
				var u = $scope.users[i];
				u.put();
			}
			$('#boardModal').modal('toggle');
		});
	}

	$scope.newuser = {'username': '', 'read': false, 'write': false, 'admin': false};

	$scope.saveUser = function() {
		return Restangular.one('boards', $routeParams['id']).customPOST($scope.newuser, 'users').then(function(data) {
			$scope.users.push(data);
			$scope.newuser = {'username': '', 'read': false, 'write': false, 'admin': false};
		});
	};

	// Create new post
	$scope.save_post = function() {
		$scope.newPost.important = false;
		$scope.newPost.board = $scope.board.id;
		Restangular.one('posts').customPOST($scope.newPost).then(function(postedData) {
			$scope.newPost.subject = "";
			$scope.newPost.content = "";
			$scope.posts.push(postedData);
			$("#newPostModal").modal("toggle");
		});
	};

	$scope.$on('logout', function(event) {
			$scope.posts = null;
			$scope.users = null;
			$scope.board = null;
			$scope.newPost = null;
	});

	Restangular.one('boards', $routeParams['id']).customGET('favourite').then(function (data) {
		$scope.isFavourited = data;
	});
	
	$scope.add_fav = function() {
		$scope.isFavourited.favourite = !$scope.isFavourited.favourite;
		Restangular.one('boards', $routeParams['id']).customPOST($scope.isFavourited, 'favourite');
	}

	$scope.remove_fav = function() {
		$scope.isFavourited.favourite = !$scope.isFavourited.favourite;
		Restangular.one('boards', $routeParams['id']).customDELETE('favourite');
	}

}]);

BoardCtrl.controller('BoardSettingsCtrl', ['$scope', function($scope) {
	$scope.cname = "board_settings";
}]);

BoardCtrl.controller('CreateBoardCtrl', ['$scope', function($scope) {
	$scope.cname = "create_board";
}]);
