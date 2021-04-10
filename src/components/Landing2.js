import React, { Component } from 'react'
import { Redirect } from "react-router-dom";

class Landing extends Component {
  state = {
    redirect: false
  }

  componentDidMount() {
    this.id = setTimeout(() => this.setState({ redirect: true }), 4000)
  }
  
  componentWillUnmount() {
    clearTimeout(this.id)
  }

  

  render() {
    return (
     <div >
        <div style={{ position:'absolute', top:"70%", left:" 40%" }}>
            
            {this.state.redirect
              ? <Redirect to="/welcome" />
              : <div>GETTING READY</div>}
        </div>
      </div>
    )
  }
}

export default Landing
