import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Navbar from "./components/Navbar";
import NewStory from "./pages/Content/index";
import Profile from "./pages/Profile/Profile";
import { Account } from "./pages/Profile/Account";
import PageNotFound from "./pages/Php";
import { Draft } from "./pages/Profile/Draft";
import { Published } from "./pages/Profile/Published";
import { Respond } from "./pages/Profile/Responses";
import "react-toastify/dist/ReactToastify.css";
import { ToastContainer } from "react-toastify";
import SearchPage from "./pages/SearchPage";

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <br />
        <br />
        <br />
        <ToastContainer
          position="top-center"
          autoClose={5000}
          hideProgressBar={false}
          newestOnTop={false}
          closeOnClick
          rtl={false}
          pauseOnFocusLoss
          draggable
          pauseOnHover
          theme="light"
        />
        <Routes>
          <Route path="/" element={<Home />} exact />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/new-story" element={<NewStory />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/profile/account" element={<Account />} />
          <Route path="/profile/draft" element={<Draft />} />
          <Route path="/profile/published" element={<Published/>} />
          <Route path="/profile/respond" element={<Respond />} />
          <Route path="/search" element={<SearchPage/>}/>
          <Route path="*" element={<PageNotFound/>}/>
        </Routes>
      </Router>
    </>
  );
}

export default App;

