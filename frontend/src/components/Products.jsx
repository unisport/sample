import React, { Component } from 'react';
import SingleProduct from './SingleProduct';
import Styles from './Styles'

class Products extends Component {
	constructor(props) {
		super(props);

		let page = props.location.search.split("?page=")[1]
		if (isNaN(page)) {
			page = 1;
		}

		this.state = {
			page,
			products: []
		}

		this.fetchData();
	}

	async fetchData(page=this.state.page) {
		const data =
			await fetch(`/api/products/${page}/`);
		const json = await data.json()
		this.setState({products: json})
	}

	changePage(self, count) {
		let page = parseInt(self.state.page) + count;
		if (page < 1) {
			page = 1;
		}
		self.props.history.push(`/products/?page=${page}`);
		self.setState({page: page});
		self.fetchData(page)
	}

  render() {
    return (
      <div style={{display: 'flex', flexWrap: 'wrap'}}>
      	{this.state.page !== 1 &&
      	<div style={styles.containerStyle}>
      		<p onClick={() => this.changePage(this, -1)} style={styles.linkStyle}>
      			Forrige side
      		</p>
      	</div>}

      	{this.state.products.map(product =>
      		<SingleProduct key={product.id} product={product} />)}
      	{this.state.products.length === 10 &&
      		<div style={styles.containerStyle}>
      			<p onClick={() => this.changePage(this, 1)} style={styles.linkStyle}>
      				Næste side
      			</p>
      		</div>
      	}
      	{this.state.products.length === 0 &&
      		<div>
      			<br />
	      		<h1>Der er desværre ingen produkter som passer i denne kategori</h1>
	      		<p>
	      			Du kan prøve vores andre kategorier indtil, vi fylder denne kategori
	      			ud.
	      		</p>
      		</div>
      	}
      </div>
    );
  }
}

const styles = {
	linkStyle:	{...Styles.largeText,
		textDecoration: 'underline',
		userSelect: 'none',
		cursor: 'pointer',
		MozUserSelect: 'none',
		WebkitUserSelect: 'none',
		msUserSelect: 'none',
	},
	containerStyle: {
		display: 'flex',
		flexDirection: 'column',
		justifyContent: 'center',
		width: 200,
		textAlign: 'center'
	}
}

export default Products;
