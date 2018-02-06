import React, { Component } from 'react';
import Products from './Products';

class KidsProducts extends Products {

	async fetchData(page=this.state.page) {
		const data =
			await fetch(`/api/kids/${page}/`);
		const json = await data.json()
		this.setState({products: json})
	}
}

export default KidsProducts;