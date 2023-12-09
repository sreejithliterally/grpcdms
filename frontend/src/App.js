import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/authpages/Login';
import Register from './components/authpages/Register';
import Home from './components/home/Home';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/" element={<Home />} />
      

      </Routes>
    </Router>
  );
}

export default App;
