
var app = angular.module('options', ['ui.bootstrap'])
	.run(function ($rootScope) {
	    $rootScope._ = window._;
	})
	.controller("optionCtrl", function ($scope, $http) {
		$http.get("option_values").success(function (data) {

			// Prepare the options for use in angularjs
			$scope.options = _.map(data, function (option, name) {
				var _default;
				if (option.length) {
					// find the default
					for (i=0; i<option.length; i++) {
						if (option[i].default === true) {
							_default = option[i].value;
						}
					}
					return {
						values: option,
						name: name,
						default: _default
					}
				}
				return _.extend(option, {name: name})
			});
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

		$scope.set_default = function(value) {
			debugger;
		}

		$scope.add_value = function (option) {
			if (option.values && option.values.length) {
				option.values.push({
					value: "value",
					price: 0
				})
			} else {
				this.options[this.name] = [option]
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