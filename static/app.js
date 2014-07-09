
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
	$scope.prices = {
		meat: 2.00,
		cheese: {
			NO_CHEESE: 0.00,
			CHEESE: 0.20,
			DOUBLE_CHEESE: 0.40
		},
		bacon: 0.50,
		tomatoes: 0.05,
		cucumber: 0.05,
		cabbage: 0.05,
	}
	$scope.burgers = []

	$scope.add_burger = function () {
		$scope.burgers.push({
			cheese: "CHEESE",
			meat: "MEDIUM",
			tomatoes: true,
			cucumber: true,
			cabbage: true
		})
	}

	$scope.order = function () {}
})