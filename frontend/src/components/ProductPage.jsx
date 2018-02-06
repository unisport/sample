import React, { Component } from 'react';
import Styles from './Styles';
import commaSeperate from '../helpers/commaSeperate'
import { withRouter } from 'react-router'

class ProductPage extends Component {
	constructor(props) {
		super(props);
		this.state = {
			id: props.match.params.id,
			product: {}
		}

		this.fetchData()
	}

	async fetchData() {
		const data = await fetch(`/api/${this.state.id}/`);
		console.log(data)
		const json = await data.json()
		console.log(json)
		this.setState({product: json})
	}

  render() {
    return (
    	<div>
		  <h1 style={styles.header}>{this.state.product.name}</h1>
		  <img alt={this.state.product.name} style={{maxHeight: 400, display: 'block', margin: 'auto'}} src={this.state.product['img_url']}></img>
		  <h3 style={{...Styles.largeText, textAlign: 'center'}}>
		  	{commaSeperate(this.state.product.price)}&nbsp;
		  	<span style={Styles.mediumText}>{this.state.product.currency}</span>
  	  </h3>
  	  <ul>
  	  	<li>Størrelser: {this.state.product.sizes}</li>
  	  	<li>Levering: {this.state.product.delivery}</li>
  	  </ul>
	    </div>
    );
  }
}

const styles = {
	header: {...Styles.header,
		textAlign: 'center',
		marginTop: '1em',
	}
}


export default withRouter(ProductPage);
