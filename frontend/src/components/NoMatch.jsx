import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class NoMatch extends Component {
  render() {
    return (
    	<div>
    		<br />
    		<h1>Siden kunne ikke findes</h1>
    		<br />
    		<p>
    			Brug din browsers tilbage funktion eller gå til&nbsp;
    			<Link to='/'>forsiden</Link>
    		</p>
	    </div>
    );
  }
}

export default NoMatch;
