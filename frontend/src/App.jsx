import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
// import './App.css'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import Register from './pages/Register'
import Navbar from './components/Navbar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Navbar/>
    <br/>
    <br/>
    <br/>
    <Router>
      <Routes>
        <Route path='/' element={<Home />} exact />
        <Route path='/login' element={<Login />} />
        <Route path='/register' element={<Register />} />
      </Routes>
    </Router>
    </>
  )
}

export default App
