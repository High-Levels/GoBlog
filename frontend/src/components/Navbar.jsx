import React from 'react'
import Button from './Button'
import GoblogPict from '../assets/images/Goblog.jpeg'
import Avatar from './Avatar'
import Image1 from '../assets/images/avatar.png'
import '../style/index.css'


// $(document).ready(function(){
//   $(window).scroll(function(){
//     if ($(this).scrollTop()>50){
//       $('.navbar').addClass('scrolled');
//     } else{
//       $('navbar').removeClass('scrolled')
//     }
//   });
// });
const Navbar = () => {
  return (
    <div>
      <nav className="navbar navbar-expand-sm navbar-light bg-light  fixed-top">
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
              <button className='btn dropdown-toggle' type='button' id='dropdownMenuButton' data-bs-toggle="dropdown" aria-expanded="false">
                <Avatar src={Image1} height={30} className="rounded-5"/>
              </button>
              <ul className='dropdown-menu' aria-labelledby='dropdownMenuButton'>
                <li><a className='dropdown-item' href='#'>test</a></li>
                <li><a className='dropdown-item' href='#'>test</a></li>
                <li><a className='dropdown-item' href='#'>test</a></li>
              </ul>
            </div>
          </div>
        </div>
      </nav>
    </div>
  )
}

export default Navbar