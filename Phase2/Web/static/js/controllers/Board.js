'use strict';

var BoardCtrl = angular.module('BoardCtrl', ['restangular']);


BoardCtrl.controller('BoardCtrl', ['$scope', 'Restangular', '$routeParams', function($scope, Restangular, $routeParams) {
	$scope.cname = "board";
	Restangular.one('boards', $routeParams['id']).get().then(function (board) {
		$scope.board = board;
	});

	Restangular.one('boards', $routeParams['id']).getList('posts').then(function (posts) {
		$scope.posts = posts;
		for (var i = 0; i < $scope.posts.length; i++) {
			var d = new Date($scope.posts[i].creation_date)
			$scope.posts[i].creation_date = d.toLocaleString();
		}
	});

	Restangular.one('boards', $routeParams['id']).getList('users').then(function (users) {
		$scope.users = users;
	});
	
	// Toggle user priviledges for the board
	$scope.toggle = function(user, item) {
		user[item] = !user[item];
	}

	// Update board 
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

	// Add user to the board
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
			var d = new Date(postedData.creation_date);
			postedData.creation_date = d.toLocaleString();
			$scope.posts.push(postedData);
			$("#newPostModal").modal("toggle");
		});
	};

	// Clean scope variables on logout
	$scope.$on('logout', function(event) {
			$scope.posts = null;
			$scope.users = null;
			$scope.board = null;
			$scope.newPost = null;
	});

	// Get the board's favourite status
	Restangular.one('boards', $routeParams['id']).customGET('favourite').then(function (data) {
		$scope.isFavourited = data;
	});
	
	// Add board to favourites
	$scope.add_fav = function() {
		$scope.isFavourited.favourite = !$scope.isFavourited.favourite;
		Restangular.one('boards', $routeParams['id']).customPOST($scope.isFavourited, 'favourite');
	}

	// Unfavourite the board
	$scope.remove_fav = function() {
		$scope.isFavourited.favourite = !$scope.isFavourited.favourite;
		Restangular.one('boards', $routeParams['id']).customDELETE('favourite');
	}

}]);
