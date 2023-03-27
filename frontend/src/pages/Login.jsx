import React from 'react'
import Button from '../components/Button'
import Gap from '../components/Gap'
import Input from '../components/Input'

const Login = () => {
  return (
    <div className='container-fluid h-100 mt-5'>
      <div className='row justify-content-center align-items-center h-100'>
        <div className='col-md-4'>
          <form action=''>
            <div className='card'>
              <div className='card-header'>Login Form</div>
              <div className='card-body'>
                <Input label='Email' placeholder='Enter Email' type='email' />
                <Gap height={18} />
                <Input
                  label='Password'
                  placeholder='Enter Password'
                  type='password'
                />
              </div>
              <div className='card-footer'>
                <Button label='Login' variant='success' />
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  )
}

export default Login
