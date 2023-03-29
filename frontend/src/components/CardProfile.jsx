import React from 'react';
import Avatar from './Avatar';
import Image1 from '../assets/images/avatar.png';

const CardProfile = () => {
  return (
    <div>
      <div className='card'>
        <Avatar src={Image1} height={100} />
        <h4>Duta Prima Putra</h4>

        <p>
          {' '}
          <a style={{ textDecoration: 'none', color: 'green' }} href=''>
            Edit Profile
          </a>
        </p>
      </div>
    </div>
  )
}

export default CardProfile;
