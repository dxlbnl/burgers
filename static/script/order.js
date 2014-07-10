
var app = angular.module('order', ['ui.bootstrap'])
	.run(function ($rootScope) {
	    $rootScope._ = window._;
	})
	.controller('OrderCtrl', function ($scope, $http) {

		$http.get("option_values").success(function (data) {
			$scope.options = data;
		})

		$scope.order = {
			address : { "name": "Dexter", "street": "Klopsteen 8", "place": "Den Haag", "postal": "2496SM" },
			burgers : []
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