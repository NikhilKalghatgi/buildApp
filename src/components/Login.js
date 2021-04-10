import React, { Component } from 'react'


class Login extends Component {
  constructor() {
    super()
    this.state = {
      email: null,
      password: '',
      errors: undefined,
      errorMessage: undefined,
      landing_page : ""
    }
  }

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value })
  }

  onSubmit = (e) => {
    e.preventDefault()
    
  }


  render() {
    return (
      <div id="background-img"  >
        <form validate onSubmit={this.onSubmit}>
          <div className="container">
            <label for="email"><b>Email</b></label>
            <input 
              type="email" 
              placeholder="Enter Email" 
              name="email" 
              value={this.state.email}
							onChange={this.onChange}
              required 
            />

            <label for="password"><b>Password</b></label>
            <input 
              type="password" 
              placeholder="Enter Password" 
              name="password" 
              value={this.state.password}
							onChange={this.onChange}
              required 
            />
                
            <button type="submit">Login</button>
            <label>
              <input type="checkbox" checked="checked" name="remember" /> Remember me
            </label>
          </div>

          <div className="container" style={{background:"#f1f1f1"}}>
            <button type="button" className="cancelbtn">Cancel</button>
            {/* <span className="psw">Forgot <a href="#">password?</a></span> */}
          </div>
        </form>
      </div>
      
    )
  }
}
export default Login