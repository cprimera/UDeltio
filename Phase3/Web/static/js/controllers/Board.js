'use strict';

var BoardCtrl = angular.module('BoardCtrl', ['restangular']);

BoardCtrl.filter('localeString', function () {
	return function(input) {
		return input.toLocaleString();
	}
});


BoardCtrl.controller('BoardCtrl', ['$scope', '$rootScope', 'Restangular', '$routeParams', function($scope, $rootScope, Restangular, $routeParams) {
	$scope.cname = "board";
	Restangular.one('boards', $routeParams['id']).get().then(function (board) {
		$scope.board = board;
		$scope.publicBoard = board.public; // temporary variable to avoid data binding on unsaved data
	});

	Restangular.one('boards', $routeParams['id']).getList('posts').then(function (posts) {
		$scope.posts = posts;
		for (var i = 0; i < $scope.posts.length; i++) {
			var d = new Date($scope.posts[i].creation_date)
			$scope.posts[i].creation_date = d;
		}
	});

	Restangular.one('boards', $routeParams['id']).getList('users').then(function (users) {
		$scope.users = users;
	});


	$scope.canPost = false;
	$scope.isAdmin = false;
	// Get current user permissions
	Restangular.one('boards', $routeParams['id']).one("users", $rootScope.currentUser.id).get().then(function (user) {
		$scope.canPost = user.write || user.admin;
		$scope.isAdmin = user.admin;
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
				if ($scope.users[i].id == $rootScope.currentUser.id) {
					$scope.canPost = $scope.users[i].write || $scope.users[i].admin;
					$scope.isAdmin = $scope.users[i].admin;
				}
			}
			$scope.board = data;
			$('#boardModal').modal('toggle');
			$scope.publicBoard = data.public;
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


	$scope.postDetails = {'important': false, 'board': $routeParams['id'], 'subject': "", 'content': "", 'offensive': false};

	// Create or update post
	$scope.savePost = function() {
		if ($scope.newPost) {
			Restangular.one('posts').customPOST($scope.postDetails).then(function(postedData) {
				$scope.clearPost();
				var d = new Date(postedData.creation_date);
				postedData.creation_date = d;
				$scope.posts.push(postedData);
			});
		} else {
			$scope.editedPost.subject = $scope.postDetails.subject;
			$scope.editedPost.content = $scope.postDetails.content;

			Restangular.one('posts', $scope.editedPost.id).customPUT($scope.editedPost).then(function(postedData) {
				$scope.clearPost();
			});
		}
	};

	$scope.clearPost = function() {
		$scope.newPost = true;
		$scope.postDetails = {'important': false, 'board': $routeParams['id'], 'subject': "", 'content': "", 'offensive': false};
	}

	$scope.updatePostDetails = function(post) {
		$scope.newPost = false;
		$scope.editedPost = post;
		$scope.postDetails.subject = post.subject;
		$scope.postDetails.content = post.content;
	};

	$scope.deletePost = function(post) {
		Restangular.one('posts', post.id).remove().then(function() {
	    	$scope.posts = _.without($scope.posts, post);
	   });
	};

	// Clean scope variables on logout
	$scope.$on('logout', function(event) {
			$scope.posts = null;
			$scope.users = null;
			$scope.board = null;
			$scope.newPost = null;
			$scope.postDetails = null;
	});

	// Get the board's favourite status
	Restangular.one('boards', $routeParams['id']).customGET('favourite').then(function (data) {
		$scope.isFavourited = data;
	});
	
	// Add board to favourites
	$scope.addFavourite = function() {
		$scope.isFavourited.favourite = !$scope.isFavourited.favourite;
		Restangular.one('boards', $routeParams['id']).customPOST($scope.isFavourited, 'favourite');
	}

	// Unfavourite the board
	$scope.removeFavourite = function() {
		$scope.isFavourited.favourite = !$scope.isFavourited.favourite;
		Restangular.one('boards', $routeParams['id']).customDELETE('favourite');
	}
	
	// Flag a post
	$scope.flagPost = function(post) {
		$scope.editedPost = post;
		$scope.editedPost.offensivePost = !$scope.editedPost.offensivePost;
		Restangular.one('posts', post.id).customPUT($scope.editedPost).then(function() {
		});
	};

}]);
