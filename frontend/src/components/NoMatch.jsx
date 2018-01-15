import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class NoMatch extends Component {
  render() {
    return (
    	<div>
    		<br />
    		<h1>Page could not be found</h1>
    		<br />
    		<p>
    			Try using the browsers back function or go to the&nbsp;
    			<Link to='/'>hompage</Link>
    		</p>
	    </div>
    );
  }
}

export default NoMatch;
