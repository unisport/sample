(function(){
	'use strict';

	angular
		.module('app.products')
		.controller('ProductController', ProductController)
		.controller('KidsProductsController', KidsProductsController)
		.controller('ProductsController', ProductsController);

	/*jshint latedef:nofunc*/
	ProductController.$inject = ['item'];
	function ProductController(item) {
		/*jshint validthis:true*/
		var vm = this;
		vm.item = item;
	}

	/*jshint latedef:nofunc*/
	ProductsController.$inject = ['items', '$state', '$window'];
	function ProductsController(items, $state, $window){
		/*jshint validthis:true*/
		var vm = this;
		$window.scrollTo(0, 0);
		vm.title = 'Products: All';
		vm.products = items.products;
		vm.count = items.count;
		vm.current_page = items.current_page;
		vm.total_pages = items.pages;
		vm.page_size = 10;
		vm.items_per_page = 10;


		vm.change_page = function() {
			if (vm.current_page === 1) {
				$state.go('index', {page:null});
			} else {
				$state.go('index', {page:vm.current_page});
			}
		};
	}

	/*jshint latedef:nofunc*/
	KidsProductsController.$inject = ['items', '$state', '$window'];
	function KidsProductsController(items, $state, $window){
		/*jshint validthis:true*/
		var vm = this;
		$window.scrollTo(0, 0);
		vm.title = 'Products: Kids';
		vm.products = items.products;

		vm.change_page = function() {
			if (vm.current_page === 1) {
				$state.go('kidsproducts', {page:null});
			} else {
				$state.go('kidsproducts', {page:vm.current_page});
			}
		};
	}
})();