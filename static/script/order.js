
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
			// create a new object out of the defaults.
			$scope.order.burgers.push(
				_.object(_.keys($scope.options), 
					_.map($scope.options, function get_default(opt) {
						// return the default
						if (opt.default) {
							return opt.default;
						} else if (opt.length) {
							for (i=0; i<opt.length; i++) {
								if (opt[i].default) return opt[i].value;
							}
						}
					})
				)
			);
		}

		$scope.price = function (burger) {
			// Map burger on scheme, and add the prices
			var price = 0;

			return _.reduce(burger, function (result, value, ingredient) {
				var option;
				if (value) {
					option = $scope.options[ingredient];
					if (_.isArray(option)) {
						return result + _.findWhere(option, {value: value}).price;
					} else if (option && option.price) {
						return result + option.price;
					}
				}
				return result;
			}, 0)
		}
		$scope.total = function () {
			var burgers = _.map($scope.order.burgers, $scope.price);


			return _.reduce(burgers, function (a, b) {return a+b}, 0)
		}
	});











// <!-- 
// 					<select ng-model='burger.meat' class='form-control'>
// 						<option ng-repeat="(key, value) in OPTIONS.meat" value="{{key}}">{{value}}</option>
// 					</select>
// 					<select ng-model='burger.cheese' class='form-control'>
// 						<option ng-repeat=	"(key, value) in OPTIONS.cheese" value="{{key}}">{{value}}</option>
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