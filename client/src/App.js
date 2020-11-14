import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import AppNavbar from './components/AppNavbar'
import { BrowserRouter as Router, Route, Switch, Link, Redirect } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <AppNavbar />
        <div className="page-content">
          Das ist deine neue, tolle Webseite!
          </div>
      </Router>
    </div>
  );
}

export default App;
