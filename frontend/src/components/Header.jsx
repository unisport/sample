import React, { Component } from 'react';
import { withRouter } from 'react-router'
import { Link } from 'react-router-dom'
import '../App.css'

class Header extends Component {
  render() {
    return (
			<header style={styles.header}>
        <Link style={styles.link} to='/'>Hjem</Link>
        <Link style={styles.link} to='/products/'>Produkter</Link>
        <Link style={styles.link} to='/kids/'>Børn</Link>
      </header>
    );
  }
}

const styles = {
	header: {
		padding: '0 5vw',
		gridArea: 'header',
		background: '#3A74A7',
		color: 'white',
		display: 'flex',
		justifyContent: 'flex-start'
	},
	link: {
		display: 'flex',
		alignItems: 'center',
		color: 'white',
		padding: '0 0.5em',
		textAlign: 'center'
	}
}


export default withRouter(Header);
