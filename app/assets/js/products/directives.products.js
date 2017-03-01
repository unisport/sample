(function(){
	'use strict';

	angular
		.module('app.products')
		.directive('usProducts', usProducts)
		.directive('usProduct', usProduct);

	/*jshint latedef:nofunc*/
	usProducts.$inject = [];
	function usProducts() {
		return {
			restrict: 'AE',
			templateUrl: 'assets/js/products/templates/_product_list.html'
		};
	}

	/*jshint latedef:nofunc*/
	usProduct.$inject = [];
	function usProduct() {
		return {
			restrict: 'AE',
			templateUrl: 'assets/js/products/templates/_product.html'
		};
	}
})();