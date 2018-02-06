import React, { Component } from 'react';
import { Route, Switch } from 'react-router';
import Products from './components/Products'
import KidsProducts from './components/KidsProducts'
import Header from './components/Header'
import Footer from './components/Footer'
import Index from './components/Index'
import NoMatch from './components/NoMatch'
import ProductPage from './components/ProductPage'
import './App.css'

class App extends Component {
  render() {
    return (
    	<div id="container" style={containerStyle}>
    		<Header />
    		<main style={{gridArea: 'main'}}>
	    		<Switch>
					<Route exact path="/" component={Index} />
					<Route exact path="/products/" component={Products} />
					<Route exact path="/products/:id/" component={ProductPage} />
					<Route exact path="/kids/" component={KidsProducts} />
					<Route component={NoMatch} />
				</Switch>
			</main>
			<Footer />
		</div>
    );
  }
}

const containerStyle = {
	minWidth: '100vw',
	minHeight: '100vh',
	display: 'grid',
	gridTemplateColumns: '5vw 90vw 5vw',
	gridTemplateRows: '80px 9fr auto',
	gridTemplateAreas: `
		"header header header"
		". main ."
		"footer footer footer"`
}

export default App;
