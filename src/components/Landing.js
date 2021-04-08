import React, { Component } from 'react'


class Landing extends Component {
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
