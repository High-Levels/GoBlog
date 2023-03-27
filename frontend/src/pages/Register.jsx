import React from 'react'
import Button from '../components/Button'
import Gap from '../components/Gap'
import Input from '../components/Input'
import ImageLogin from '../assets/images/Image-login.jpg'
import '../style/index.css'

const Login = () => {
  return (
    <div>
      <div className='row justify-content-center align-items-center h-100'>
        <div className='col-md-10 mt-5'>
          <div className='card'>
            <div className='row'>
              <div className='col-md-8'>
                <img
                  src={ImageLogin}
                  className='img-fluid rounded'
                  style={{}}
                />
              </div>
              <div className='col-md-4 d-flex align-items-center'>
                <div className='card-body me-4'>
                  <form action=''>
                    <h2 className='text-center'>Register </h2>
                    <Input
                      label='Username'
                      placeholder='Enter Username'
                      type='username'
                    />
                    <Gap height={18} />
                    <Input
                      label='Email'
                      placeholder='Enter Email'
                      type='email'
                    />
                    <Gap height={18} />
                    <Input
                      label='Password'
                      placeholder='Enter Password'
                      type='password'
                    />
                    <Gap height={18} />
                    <Button label='Login' variant='success' width='w-100' />
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Login
