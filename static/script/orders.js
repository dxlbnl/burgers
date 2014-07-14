
var app = angular.module('orders', ['ui.bootstrap'])
	.run(function ($rootScope) {
	    $rootScope._ = window._;
	})
	.controller('orderListCtrl', function ($scope, $http) {
		$http({
			method: "GET",
			url: 'orders',
		}).success(function (data) {
			$scope.orders = data;
		})

		$scope.price = function (object, store_obj) {
			// calculate the price of object, either in an object contained in an array, or contianed in an object
			// also stores the price in the object

			store_obj = object || store_obj;

			store_obj.price = _(
				_(object).pluck('price')
			).reduce(function (a, b) {return (b || 0) + a;}, 0)

			return store_obj.price
		}
		$scope.filter_price = function (burger) {
			// we have to filter the price out of the burger;
			return  _(burger).omit('price')
		}
	})