import React from 'react';
import Button from './Button';
import GoblogPict from '../assets/images/Goblog.jpeg';
import Avatar from './Avatar';
import Image1 from '../assets/images/avatar.png';
import '../style/index.css';


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
                <a className="nav-link" href="/register"> <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-chat-right-quote"
                viewBox="0 0 16 16"
              >
                <path d="M2 1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h9.586a2 2 0 0 1 1.414.586l2 2V2a1 1 0 0 0-1-1H2zm12-1a2 2 0 0 1 2 2v12.793a.5.5 0 0 1-.854.353l-2.853-2.853a1 1 0 0 0-.707-.293H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12z" />
                <path d="M7.066 4.76A1.665 1.665 0 0 0 4 5.668a1.667 1.667 0 0 0 2.561 1.406c-.131.389-.375.804-.777 1.22a.417.417 0 1 0 .6.58c1.486-1.54 1.293-3.214.682-4.112zm4 0A1.665 1.665 0 0 0 8 5.668a1.667 1.667 0 0 0 2.561 1.406c-.131.389-.375.804-.777 1.22a.417.417 0 1 0 .6.58c1.486-1.54 1.293-3.214.682-4.112z" />
              </svg></a>
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

export default Navbar;