import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Footer extends Component {
  render() {
    return (
    	<footer style={styles.footer}>
        	<p>
        		Website developed by&nbsp;
        		<Link to='https://github.com/BeneCollyridam' style={styles.link}>
        			Alexaxander M. Scheurer
    			  </Link>
        	</p>
      	</footer>
    );
  }
}

const styles = {
  footer: {
    gridArea: 'footer',
    background: '#3C3C38',
    color: 'white',
    display: 'inline-flex'
  },
  link: {
    color: 'white'
  }
}

export default Footer;