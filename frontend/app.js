var app = angular.module('stringCalcApp', []);

app.controller('CalculatorController', function($http) {
  var vm = this;
  vm.input = "";
  vm.result = null;
  vm.error = "";

  vm.calculate = function() {
    vm.result = null;
    vm.error = "";

    $http.post('http://127.0.0.1:8000/api/calculate', { numbers: vm.input })
      .then(function(response) {
        vm.result = response.data.result;
      })
      .catch(function(error) {
        if (error.data && error.data.detail) {
          vm.error = error.data.detail;
        } else {
          vm.error = "Server error. Please try again.";
        }
      });
  };
});
