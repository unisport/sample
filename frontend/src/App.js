import React, { Component } from 'react';
import { Route, Switch } from 'react-router';
import Products from './components/Products'
import Header from './components/Header'
import Footer from './components/Footer'
import Index from './components/Index'
import NoMatch from './components/NoMatch'
import './App.css'

class App extends Component {
  render() {
    return (
    	<div id="container">
    		<Header />
    		<main>
	    		<Switch>
					<Route exact path="/" component={Index} />
					<Route path="/products/:page?" component={Products} />
					<Route component={NoMatch} />
				</Switch>
			</main>
			<Footer />
		</div>
    );
  }
}

export default App;
