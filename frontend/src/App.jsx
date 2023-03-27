import { Component, useState } from 'react'
import Particle from './components/Particles.BG'
import { BrowserRouter as Router, Route, Routes, } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import Register from './pages/Register'
import Navbar from './components/Navbar'


function App() {
  const [count, setCount] = useState(0);
  return (
    <>
    <Particle/>
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
