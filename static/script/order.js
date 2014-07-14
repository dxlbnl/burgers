
var app = angular.module('order', ['ui.bootstrap'])
	.run(function ($rootScope) {
	    $rootScope._ = window._;
	})
	.controller('OrderCtrl', function ($scope, $http) {

		$http.get("ingredients_list").success(function (data) {
			$scope.ingredients = data;
		})

		$scope.order = {
			address : { "name": "Dexter", "street": "Klopsteen 8", "place": "Den Haag", "postal": "2496SM" },
			burgers : []
		};

		$scope.add_burger = function () {
			// create a new object out of the defaults.
			$scope.order.burgers.push(
				_.object(_.pluck($scope.ingredients, 'name'), 
					_.map($scope.ingredients, function get_default(opt) {
						var i;
						// return the default
						if (opt.default) {
							return opt.default;
						} else if (opt.values) {
							for (i=0; i<opt.values.length; i++) {
								if (opt.values[i].default) return opt.values[i].value;
							}
						}
					})
				)
			);
		}

		$scope.price = function (burger) {
			// Map burger on scheme, and add the prices
			var i, ingredient, price = 0;

			for (i=0; i<$scope.ingredients.length; i++) {
				ingredient = $scope.ingredients[i];
				if (burger.hasOwnProperty(ingredient.name)) {
					if (ingredient.values) {
						price += _.findWhere(ingredient.values, {value: burger[ingredient.name]}).price;
					} else if (burger[ingredient.name] === true) {
						price += ingredient.price;
					}
				}
			}
			return price;

		}
		$scope.total = function () {
			var burgers = _.map($scope.order.burgers, $scope.price);


			return _.reduce(burgers, function (a, b) {return a+b}, 0)
		}
	});











// <!-- 
// 					<select ng-model='burger.meat' class='form-control'>
// 						<option ng-repeat="(key, value) in ingredients.meat" value="{{key}}">{{value}}</option>
// 					</select>
// 					<select ng-model='burger.cheese' class='form-control'>
// 						<option ng-repeat=	"(key, value) in ingredients.cheese" value="{{key}}">{{value}}</option>
// 					</select>
// 					<div class='btn-group'>
// 						<label class='btn btn-primary' ng-model="burger.bacon" btn-checkbox>bacon</label>
// 						<label class='btn btn-primary' ng-model="burger.tomatoes" btn-checkbox>tomatoes</label>
// 						<label class='btn btn-primary' ng-model="burger.cucumber" btn-checkbox>cucumber</label>
// 						<label class='btn btn-primary' ng-model="burger.cabbage" btn-checkbox>cabbage</label>
// 					</div>
//  -->
// 	<!-- 				<span class='right'>

// 						<div class='input-group'>
// 							<label class='input-group-addon' for='addrName'>Price: </label>
// 							<input id='addrName' class='form-control' type='text' disabled value='{{price(burger) | currency : "€"}}'/>
// 						</div>
// 						<label class='remove btn btn-danger' ng-click="burgers.splice($index,1)">Remove</label>
// 					</span> -->