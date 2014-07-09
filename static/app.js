
var app = angular.module('order', ['ui.bootstrap'])
	.run(function ($rootScope) {
	    $rootScope._ = window._;
	})
	.controller('OrderCtrl', function ($scope) {
		$scope.OPTIONS = {
			meat: {
				R: "Rare",
				M: "Medium",
				W: "Well done"
			}, 
			cheese: {
				NC: "No cheese",
				C:  "Cheese",
				DC: "Double cheese"
			}
		};
		$scope.pricing_scheme = {
			base_price: 2.00,
			meat: 2.00,
			cheese: {
				NC: 0.00,
				C: 0.20,
				DC: 0.40
			},
			bacon: 0.50,
			tomatoes: 0.10,
			cucumber: 0.10,
			cabbage: 0.10,
		};

		$scope.order = {
			address : { "name": "Dexter", "street": "Klopsteen 8", "place": "Den Haag", "postal": "2496SM" },
			burgers : [{
				cheese: "C",
				meat: "M",
				tomatoes: true,
				cucumber: true,
				cabbage: true
			}]
		};

		$scope.add_burger = function () {
			$scope.order.burgers.push({
				cheese: "C",
				meat: "M",
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
			var burgers = _.map($scope.order.burgers, $scope.price);


			return _.reduce(burgers, function (a, b) {return a+b}, 0)
		}
	});