import React, { Component } from 'react';
import Styles from './Styles';
import commaSeperate from '../helpers/commaSeperate'
import { Link } from 'react-router-dom'
import { withRouter } from 'react-router'

class SingleProduct extends Component {
	constructor(props) {
		super(props);
		this.state = {
			product: props.product,
		}
	}

  render() {
    return (
		  <Link to={`/products/${this.state.product.id}/`}>
		    <div style={styles.container}>
		    	<div style={{position: 'relative'}}>
		    		{this.state.product["discount_type"] !== "None" &&
		    		<div style={{position: 'absolute', right: 40, top: 20, background:"yellow", color: "black", padding: 10, textAlign: 'center'}}>
		    		-{Math.floor(this.state.product.price/this.state.product['price_old'])}%
		    		</div>}
		    		<img alt={`Thumbnail for ${this.state.product.name}`} src={this.state.product.thumbnail} width={200} />
		    	</div>
		    	<p style={styles.price}>
		    		{commaSeperate(this.state.product.price)}&nbsp;
		    		<span style={Styles.smallText}>{this.state.product.currency}</span>
		    	</p>
		    	<p style={styles.name}>{this.state.product.name}</p>
		    </div>
		  </Link>
    );
  }
}

const styles = {
	container: {
		width: 200,
		display: 'inline-block',
		margin: '1em'
	},
	price: {...Styles.mediumText,
		color: "#0F0",
		textAlign: 'center'
	},
	name: {...Styles.smallText,
		color: "#000"
	}
}



export default withRouter(SingleProduct);
