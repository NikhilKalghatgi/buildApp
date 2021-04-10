import React, { Component } from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import Login from './components/Login'

import Landing from './components/Landing'
import Landing2 from './components/Landing2'

// import PrivateRoute from './PrivateRoute/PrivateRoute'

class App extends Component {

  render() {
    const Container = () => (
       <div>
          
          {/* <PrivateRoute exact path="/welcome" component={Landing} /> */}
          <Route exact path="/welcome" component={Landing} />
          <Route exact path="/" component={Login} />
          <Route exact path="/login" component={Login} />
          <Route exact path="/register" component={Landing2} />          
          
        </div>
   )
    return (
      <Router>
        <Switch>
            <div className="App">
              <Route component={Container} />
            </div>
        </Switch>
      </Router>
    )
  }
}

export default App
