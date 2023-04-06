import React, { Component } from 'react';
import Card from '../../components/Card';
import Profile from './Profile';
import Gap from '../../components/Gap';

export const Published = () => {
  return (
    <div>
    <Profile />
      <Card />
      <Gap />
      <Card />
    </div>
  )
}
