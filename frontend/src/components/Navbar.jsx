import React from 'react'
import Button from './Button'
import GoblogPict from '../assets/images/Goblog.jpeg'


const Navbar = () => {
  return (
    <div>
        <nav class="navbar navbar-expand-sm navbar-dark bg-dark fixed-top">
  <div class="container-fluid">
    <a class="navbar-brand" href="/"><img src={GoblogPict} style={{width:"150px"}}/></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mynavbar">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="mynavbar">
      <ul class="navbar-nav me-auto">
        <li class="nav-item">
          <a class="nav-link" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/login">Login</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/register">Register</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="text" placeholder="Search"/>
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