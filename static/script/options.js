
var app = angular.module('options', ['ui.bootstrap'])
	.run(function ($rootScope) {
	    $rootScope._ = window._;
	})
	.controller("optionCtrl", function ($scope, $http) {
		$http.get("option_values").success(function (data) {

			// Prepare the options for use in angularjs
			$scope.options = data;

			// Fix the defaults
			_.each($scope.options, function (option) {
				var i;
				if (option.values) {
					for (i=0; i<option.values.length; i++) {
						if (option.values[i].default) {
							option.default = option.values[i].value;
						}
					}
				}
			})
		})

		// $scope.track


		$scope.new_option = function () {
			$scope.options.push({
				name: "New",
				value : "Rare", 
				price: 2.00,
			});
		}

		$scope.prepare_options = function (options) {
			// Turn the options, a list of objects into a object with key/value options.
			var i, j, option, opts = {}
			if (options) {
				for (i=0; i<options.length; i++) {
					option = options[i];

					// Make the new option the list of values, or the value only.
					if (option.values) {
						// set the default
						for (j=0; j<option.values.length; j++) {
							if (option.default && (option.default === option.values[j].value)) {
								option.values[j].default = true;
							} else {
								option.values[j].default = false;
							}
						}

						opts[option.name] = option.values;

					} else {
						opts[option.name] = _.omit(option, 'name');
					}
				};
				
			}
			return opts
		}

		$scope.default = function(value) {
			debugger;
		}

		$scope.add_value = function (option) {
			if (option.values && option.values.length) {
				option.values.push({
					value: option.name,
					price: option.price || 0
				})
			} else {
				option.values = [{
					value: option.name,
					price: option.price || 0
				}];
			}
		}
		$scope.remove_value = function (value) {
			// 	Make the option a boolean when all the values are removed.
			if (this.option.values && this.option.values.length === 1) {
				this.option.price = value.price;
				this.option.default = value.default;

				delete this.option.values
			} else {
				this.option.values.splice(this.$index, 1);
			}
		}


		$scope.save = function () {
			$("form.hidden").submit();
		}
	})