(function(){
	'use strict';

	angular
		.module('app', [
			'ngResource',
			'ui.router',
			'ui.bootstrap',
			'app.products'
		])
		.config(routeConfig);

	/*jshint latedef:nofunc*/
	routeConfig.$inject = ['$urlRouterProvider', '$stateProvider', '$locationProvider'];
	function routeConfig($urlRouterProvider, $stateProvider, $locationProvider) {
		$urlRouterProvider
		.otherwise('/');
		$stateProvider
		.state('index', {
			url: '/?page',
			templateUrl: 'assets/js/index/templates/_index.html',
			resolve: {
				items: ['ProductService', '$stateParams', function(ProductService, $stateParams){
					return ProductService.query({id:$stateParams.id, page:$stateParams.page}).$promise;
				}]
			},
			controller: 'ProductsController',
			controllerAs: 'vm'
		})
		.state('kidsproducts', {
			url: '/products/kids/?page',
			templateUrl: 'assets/js/index/templates/_index.html',
			resolve: {
				items: ['KidsProductService', '$stateParams', function(KidsProductService, $stateParams){
						return KidsProductService.query({page:$stateParams.page}).$promise;
				}]
			},
			controller: 'KidsProductsController',
			controllerAs: 'vm'
		})
		.state('product_detail', {
			url: '/products/:item_id/',
			templateUrl: 'assets/js/products/templates/_detail.html',
			resolve: {
				item: ['ProductService', '$stateParams', function(ProductService, $stateParams){
					return ProductService.get({item_id:$stateParams.item_id}).$promise;
				}]
			},
			controller: 'ProductController',
			controllerAs: 'vm'
		})
		;
		$locationProvider.html5Mode(true);
	}


	angular.element(document).ready(function() {
        angular.bootstrap(document, ['app']);
    });
})();