import React from 'react'
import Avatar from '../components/Avatar'
import Image1 from '../assets/images/avatar.png'

const Home = () => {
  return (
    <div className='container'>
      <h1>Avatar</h1>
      <Avatar src={Image1} height={40} />
    </div>
  )
}

export default Home
