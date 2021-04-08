import React, { Component } from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import Landing from './components/Landing'

// import PrivateRoute from './PrivateRoute/PrivateRoute'

class App extends Component {

  render() {
    const Container = () => (
       <div>
          
          {/* <PrivateRoute exact path="/welcome" component={Landing} /> */}
          <Route exact path="/welcome" component={Landing} />
          
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
