import React, { Component } from 'react';
import { withRouter } from 'react-router'
import { Link } from 'react-router-dom'

class Header extends Component {
  render() {
    return (
    	<header>
        <Link to='/'>Home</Link>
        <Link to='/prod'>Products</Link>
      </header>
    );
  }
}

export default withRouter(Header);
