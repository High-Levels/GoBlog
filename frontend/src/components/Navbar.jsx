import React from 'react';
import Button from './Button';
import GoblogPict from '../assets/images/Goblog.jpeg';
import Avatar from './Avatar';
import Image1 from '../assets/images/avatar.png';
import '../style/index.css';
import Search from './Search';



const Navbar = () => {
  // const navigasi = useNavigate();
  return (
    <div>
      <nav className="navbar navbar-expand-sm navbar-light bg-light  fixed-top">
        <div className="container-fluid">
          <a className="navbar-brand" href="/"><img src={GoblogPict} style={{ width: "150px" }} /></a>
          <a href='/' className='btn d-block d-sm-none'>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                  <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z" />
                </svg>
              </a>
          <form class="form-inline my-2 my-lg-0 d-none d-lg-block">
            <Search/>
          </form>
          <div>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pen" viewBox="0 0 16 16">
              <path d="m13.498.795.149-.149a1.207 1.207 0 1 1 1.707 1.708l-.149.148a1.5 1.5 0 0 1-.059 2.059L4.854 14.854a.5.5 0 0 1-.233.131l-4 1a.5.5 0 0 1-.606-.606l1-4a.5.5 0 0 1 .131-.232l9.642-9.642a.5.5 0 0 0-.642.056L6.854 4.854a.5.5 0 1 1-.708-.708L9.44.854A1.5 1.5 0 0 1 11.5.796a1.5 1.5 0 0 1 1.998-.001zm-.644.766a.5.5 0 0 0-.707 0L1.95 11.756l-.764 3.057 3.057-.764L14.44 3.854a.5.5 0 0 0 0-.708l-1.585-1.585z" />
            </svg>
          </div>
          <div className='dropdown'>
            <button className='btn dropdown-toggle' type='button' id='dropdownMenuButton' data-bs-toggle="dropdown" aria-expanded="false">
              <Avatar src={Image1} height={30} className="rounded-5" />
            </button>
            <ul className='dropdown-menu' aria-labelledby='dropdownMenuButton'>
              <li><a className='dropdown-item' href='/register'>Registrasi</a></li>
              <li><a className='dropdown-item' href='/login'>Login</a></li>
              <li><a className='dropdown-item' href='/'>Setting</a></li>
            </ul>
          </div>
        </div>
      </nav>
      <ul id="searchResult"></ul>
    </div>
  )
}

export default Navbar;