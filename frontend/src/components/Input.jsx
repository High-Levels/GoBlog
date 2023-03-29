import React from 'react';

const Input = ({ label, ...rest }) => {
  return (
    <div>
      <div className='form-group'>
        <label htmlFor='email'>{label}</label>
        <input {...rest} className='form-control' />
      </div>
    </div>
  )
}

export default Input;
