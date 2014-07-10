
var app = angular.module('options', ['ui.bootstrap'])
	.run(function ($rootScope) {
	    $rootScope._ = window._;
	})
	.controller("optionCtrl", function ($scope, $http) {
		$http.get("option_values").success(function (data) {
			$scope.options = data;
		})


		$scope.new_option = function () {
			$scope.options.push({
				name: "TEST",
				values: [
					{value : "Rare", price: 2.00},
					{value : "Medium", price: 2.00},
					{value : "Well done", price: 2.00},
				]
			})
		}

		$scope.add_value = function (option) {
			option.values.push({
				value: "value",
				price: 0
			})
		}

		$scope.save = function () {
			$("form.hidden").submit();
		}
	})