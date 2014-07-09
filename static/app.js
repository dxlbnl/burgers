
var app = angular.module('order', ['ui.bootstrap'])
	.run(function ($rootScope) {
	    $rootScope._ = window._;
	})
	.controller('OrderCtrl', function ($scope) {
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
		$scope.pricing_scheme = {
			base_price: 2.00,
			meat: 2.00,
			cheese: {
				NO_CHEESE: 0.00,
				CHEESE: 0.20,
				DOUBLE_CHEESE: 0.40
			},
			bacon: 0.50,
			tomatoes: 0.10,
			cucumber: 0.10,
			cabbage: 0.10,
		}
		$scope.burgers = [{
				cheese: "CHEESE",
				meat: "MEDIUM",
				tomatoes: true,
				cucumber: true,
				cabbage: true
			}]

		$scope.add_burger = function () {
			$scope.burgers.push({
				cheese: "CHEESE",
				meat: "MEDIUM",
				tomatoes: true,
				cucumber: true,
				cabbage: true
			})
		}

		$scope.price = function (burger) {
			var key, 
				scheme = $scope.pricing_scheme,
				price = scheme.base_price;

			// Map burger on scheme, and add the prices
			for (key in scheme) {
				if (burger[key]) {
					if  (_.isObject(scheme[key])) {
						price += scheme[key][burger[key]];
					} else {
						price += scheme[key];
					}

				}
			}

			return price
		}
		$scope.total = function () {
			return _.reduce(
						_.map($scope.burgers, $scope.price), 
						function (a, b) {return a+b}, 0
					)
		}

		$scope.order = function () {}
	});