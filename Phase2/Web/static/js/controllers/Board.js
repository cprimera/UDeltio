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
		$scope.newPost.important = false;
		$scope.newPost.board = $scope.board.id;
		Restangular.one('posts').customPOST($scope.newPost, '', {}).then(function(postedData) {
			$scope.newPost.subject = "";
			$scope.newPost.content = "";
		});
	};

}]);




BoardCtrl.controller('BoardSettingsCtrl', ['$scope', function($scope) {
	$scope.cname = "board_settings";
}]);

BoardCtrl.controller('CreateBoardCtrl', ['$scope', function($scope) {
	$scope.cname = "create_board";
}]);