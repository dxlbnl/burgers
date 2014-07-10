
var app = angular.module('options', ['ui.bootstrap'])
	.run(function ($rootScope) {
	    $rootScope._ = window._;
	})
	.controller("optionCtrl", function ($scope, $http) {
		$http.get("option_values").success(function (data) {
			$scope.options = data;
		})




		$scope.new_option = function () {
			$scope.options.new = {
				value : "Rare", price: 2.00,
			}
		}

		$scope.set_default = function(value) {
			debugger;
		}

		$scope.add_value = function (option) {
			if (option.length) {
				option.push({
					value: "value",
					price: 0
				})
			} else {
				this.options[this.name] = [option]
			}
		}
		$scope.remove_value = function (value) {
			// 	Make the option a boolean when all the values are removed.
			if (this.option.length == 1) {
				this.options[this.name] = {
					price: value.price,
					'default': value.default
				}
			} else {
				this.option.splice(this.$index, 1);
			}
		}

		$scope.save = function () {
			$("form.hidden").submit();
		}
	})