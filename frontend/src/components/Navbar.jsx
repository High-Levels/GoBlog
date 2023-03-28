import React from 'react'
import Button from './Button'
import GoblogPict from '../assets/images/Goblog.jpeg'


const Navbar = () => {
  return (
    <div>
        <nav className="navbar navbar-expand-sm navbar-dark bg-dark fixed-top">
  <div className="container-fluid">
    <a className="navbar-brand" href="/"><img src={GoblogPict} style={{width:"150px"}}/></a>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mynavbar">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="mynavbar">
      <ul className="navbar-nav me-auto">
        <li className="nav-item">
          <a className="nav-link" href="/">Home</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="/login">Login</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="/register">Register</a>
        </li>
      </ul>
      <form className="d-flex">
        <input className="form-control me-2" type="text" placeholder="Search"/>
        <Button
        label="Search"
        variant="warning"
        />
      </form>
    </div>
  </div>
</nav>
    </div>
  )
}

export default Navbar