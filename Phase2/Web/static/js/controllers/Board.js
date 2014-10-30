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


	$scope.save_post = function() {
		console.log($scope.newPost);
		$scope.newPost.important = false;
		$scope.newPost.board = $scope.board.id;
		Restangular.all('posts').post('posts', $scope.newPost).then(function(postedData) {
			console.log("Success");
			console.log($scope.newPost);
		});
		$scope.show_add_post_modal = !$scope.show_add_post_modal;
	};


	$scope.show_add_post_modal = false;
	$scope.add_post = function() {
		$scope.show_add_post_modal = !$scope.show_add_post_modal;
	}

}]);


BoardCtrl.controller('BoardSettingsCtrl', ['$scope', function($scope) {
	$scope.cname = "board_settings";
}]);

BoardCtrl.controller('CreateBoardCtrl', ['$scope', function($scope) {
	$scope.cname = "create_board";
}]);