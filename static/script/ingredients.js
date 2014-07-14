
var app = angular.module('ingredients', ['ui.bootstrap'])
	.run(function ($rootScope) {
	    $rootScope._ = window._;
	})
	.controller("ingredientCtrl", function ($scope, $http) {
		$http.get("ingredients_list").success(function (data) {

			// Prepare the ingredients for use in angularjs
			$scope.ingredients = data;

			// Fix the defaults
			_.each($scope.ingredients, function (ingredient) {
				var i;
				if (ingredient.values) {
					for (i=0; i<ingredient.values.length; i++) {
						if (ingredient.values[i].default) {
							ingredient.default = ingredient.values[i].value;
						}
					}
				}
			})
		})

		// $scope.track


		$scope.new_ingredient = function () {
			$scope.ingredients.push({
				name: "New",
				value : "Rare", 
				price: 2.00,
			});
		}

		$scope.default = function(value) {
			debugger;
		}

		$scope.add_value = function (ingredient) {
			if (ingredient.values && ingredient.values.length) {
				ingredient.values.push({
					value: ingredient.name,
					price: ingredient.price || 0
				})
			} else {
				ingredient.values = [{
					value: ingredient.name,
					price: ingredient.price || 0
				}];
			}
		}
		$scope.remove_value = function (value) {
			// 	Make the ingredient a boolean when all the values are removed.
			if (this.ingredient.values && this.ingredient.values.length === 1) {
				this.ingredient.price = value.price;
				this.ingredient.default = value.default;

				delete this.ingredient.values
			} else {
				this.ingredient.values.splice(this.$index, 1);
			}
		}


		$scope.save = function () {
			$("form.hidden").submit();
		}
	})