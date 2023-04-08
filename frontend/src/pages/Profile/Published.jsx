import React from 'react';
import Card from '../../components/Card';
import Profile from './Profile';
import Gap from '../../components/Gap';

export const Published = () => {
  return (
    <div>
    <Profile />
      <Card />
      <Gap height={40}/>
      <Card />
    </div>
  )
}
