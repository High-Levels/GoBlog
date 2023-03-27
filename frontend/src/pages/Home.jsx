import React from 'react'
import Avatar from '../components/Avatar'
import Image1 from '../assets/images/avatar.png'
import CardProfile from '../components/CardProfile'
import Modal from '../components/Modal'
import Card from '../components/Card'
import Navbar from '../components/Navbar'

const Home = () => {
  return (
    <div className='container'>
      <Navbar />
      <h1>Avatar</h1>
      <Avatar src={Image1} height={40} />
      <hr />
      <h1>Card Profile:</h1>
      <CardProfile />
      <hr />
      <h1>Modal:</h1>
      <Modal />
      <Card />
      <Card />
      <Card />
    </div>
  )
}

export default Home
