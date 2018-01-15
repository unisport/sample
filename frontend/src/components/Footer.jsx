import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Footer extends Component {
  render() {
    return (
    	<footer>
        	<p>
        		Website developed by&nbsp;
        		<Link to='https://github.com/BeneCollyridam'>
        			Alexaxander M. Scheurer
    			</Link>
        	</p>
      	</footer>
    );
  }
}

export default Footer;