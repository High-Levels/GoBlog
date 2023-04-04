import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Navbar from "./components/Navbar";
import NewStory from "./pages/NewStory";

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <br />
        <br />
        <br />
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
