import React, { Component } from 'react';
import { Link } from 'react-router-dom'

class Index extends Component {
  render() {
    return (
      <div>
      	{/* I use h1, h2, etc because of SEO. Search engines will use this as keywords for
      	the webpage */}
        <h1>Sportstøj og -udstyr</h1>
        <br /><br />
        <h2>Kategorier</h2>
        <br />
        <Link to='/products/'><h3>Alle produkter</h3></Link>
        <Link to='/kids/'><h3>Produkter til børn</h3></Link>
      </div>
    );
  }
}

export default Index;
