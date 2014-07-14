
var app = angular.module('orders', ['ui.bootstrap'])
	.config(['$httpProvider',  function ($httpProvider) {
		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	}])
	.run(['$rootScope', function ($rootScope) {
	    $rootScope._ = window._;
	}])
	.filter('filterOrders', function() {
    	return function(orders,filter) {
      		var i, out = [];

      		if (orders) {

		  		for (i=0; i<orders.length; i++) {
		  			if (filter.status[orders[i].status] === true) {
		  				out.push(orders[i])
		  			}
		  		}
      		}
      		return out;
    	}
	})
	.controller('orderListCtrl', function ($scope, $http) {
		$scope.orderStatus = ["Ordered", "In progress", "On the road", "Delivered"];
		$scope.orderFilter = {status:{
			"Ordered" : true, "In progress" : true, "On the road" : true
		}};

		$http({
			method: "GET",
			url: 'order_list',
		}).success(function (data) {
			$scope.orders = data;
		})


		$scope.update = function (order) {

			console.log("Updating order", order)

			$http.post("order_list", {
				update: order.id,
				data: {
					status: order.status
				}
			})
		}

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