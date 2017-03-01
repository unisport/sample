(function(){
	'use strict';

	angular
		.module('app.products')
		.factory('ProductService', ProductService)
		.factory('KidsProductService', KidsProductService);

	/*jshint latedef:nofunc*/
	ProductService.$inject = ['$resource'];
	function ProductService($resource) {
		return $resource('api/products/:item_id/',
			{
				item_id: '@item_id',
				page:'@page',
			},
			{
				'get': {
					method: 'GET'
				},
				'query': {
					method: 'GET',
					isArray: false
				}
			});
	}

	/*jshint latedef:nofunc*/
	KidsProductService.$inject = ['$resource'];
	function KidsProductService($resource) {
		return $resource('api/products/kids/',
			{
				page:'@page'
			},
			{
				'query': {
					method: 'GET',
					isArray: false
				}
			});
	}
})();