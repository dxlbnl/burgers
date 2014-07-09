
var app = angular.module('order', ['ui.bootstrap']);


app.controller('OrderCtrl', function ($scope) {
	$scope.OPTIONS = {
		meat: {
			RARE: "Rare",
			MEDIUM: "Medium",
			WELL_DONE: "Well done"
		}, 
		cheese: {
			NO_CHEESE: "No cheese",
			CHEESE:  "Cheese",
			DOUBLE_CHEESE: "Double cheese"
		}
	};
	$scope.burgers = []

	$scope.add_burger = function () {
		$scope.burgers.push({
			cheese: "CHEESE",
			meat: "MEDIUM",
			bacon: false,
			tomatoes: true,
			cucumber: true,
			cabbage: true
		})
	}

	$scope.order = function () {}
})