import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import AppNavbar from './components/AppNavbar'
import NavigationPlotter from './components/NavigationPlotter'
import { BrowserRouter as Router } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <AppNavbar />
        <div className="page-content">
          <NavigationPlotter />
          </div>
      </Router>
    </div>
  );
}

export default App;
