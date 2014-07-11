
var app = angular.module('orders', ['ui.bootstrap'])
	.run(function ($rootScope) {
	    $rootScope._ = window._;
	})
	.controller('orderListCtrl', function ($scope, $http) {
		$http({
			method: "GET",
			url: 'orders',
		}).success(function (data) {
			debugger;
		})
	})