import React from 'react'
import Button from './Button'
import GoblogPict from '../assets/images/Goblog.jpeg'
import Avatar from './Avatar'
import Image1 from '../assets/images/avatar.png'


const Navbar = () => {
  return (
    <div>
      <nav className="navbar navbar-expand-sm navbar-light bg-light fixed-top">
        <div className="container-fluid">
          <a className="navbar-brand" href="/"><img src={GoblogPict} style={{ width: "150px" }} /></a>
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
              <input className="form-control me-2" type="text" placeholder="Search" />
              <Button
                label="Search"
                variant="warning"
              />
            </form>
            <div className='dropdown'>
              <Avatar src={Image1} height={40} type='button' className='dropdown-toggle' id="menu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" />
            </div>
            <ul class="dropdown-menu" role="menu" aria-labelledby="menu1">
      <li role="presentation"><a role="menuitem" tabindex="-1" href="#">HTML</a></li>
      <li role="presentation"><a role="menuitem" tabindex="-1" href="#">CSS</a></li>
      <li role="presentation"><a role="menuitem" tabindex="-1" href="#">JavaScript</a></li>
      <li role="presentation" class="divider"></li>
      <li role="presentation"><a role="menuitem" tabindex="-1" href="#">About Us</a></li>
    </ul>
          </div>
        </div>
      </nav>
    </div>
  )
}

export default Navbar