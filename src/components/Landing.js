import React, { Component } from 'react'
import { Redirect } from "react-router-dom";

class Landing extends Component {

  

  redirectFunc = () => {
    setTimeout(function () {
      return <Redirect to="/" />
    }, 5000);
  }

  render() {
    return (
     <div id="background-img">
        <div style={{ position:'absolute', top:"70%", left:" 40%" }}>
            GETTING READY
        </div>
        <div className="loader" style={{ position:'absolute', top:"69%", left:" 50%" }}></div>
      </div>
    )
  }
}

export default Landing
