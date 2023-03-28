import Particle from "./components/Particles.BG";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Navbar from "./components/Navbar";
import NewStory from "./pages/NewStory";

function App() {
  return (
    <>
      <Particle />
      <Navbar />
      <br />
      <br />
      <br />
      <Router>
        <Routes>
          <Route path="/" element={<Home />} exact />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/new-story" element={<NewStory />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
