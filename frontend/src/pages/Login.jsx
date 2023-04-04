import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import Button from '../components/Button'
import Gap from '../components/Gap'
import Input from '../components/Input'
import ImageLogin from '../assets/images/Image-login.jpg'
import Particle from '../components/Particles.BG'
import { login } from '../services/Auth'
import { toast } from 'react-toastify'

const Login = () => {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const navigate = useNavigate()

  const handleLogin = async (e) => {
    e.preventDefault()
    setIsLoading(true)

    try {
      await login(username, password)
      // alert('Login Berhasil!')
      toast.success('Login Berhasil!')
      setIsLoading(false)
      navigate('/')
    } catch (error) {
      setIsLoading(false)
      setError(error.message)
    }
  }

  return (
    <div>
      <Particle />
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
                  <form onSubmit={handleLogin}>
                    <h2 className='text-center'>Login</h2>
                    <Input
                      label='Username'
                      type='text'
                      id='username'
                      name='username'
                      value={username}
                      onChange={(e) => setUsername(e.target.value)}
                    />

                    <Gap height={18} />

                    <Input
                      label='Password'
                      type='password'
                      id='password'
                      name='password'
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                    />

                    {error && (
                      <>
                        <Gap height={18} />
                        <div className='alert alert-danger'>{error}</div>
                      </>
                    )}

                    <Gap height={18} />

                    <Button
                      label={isLoading ? 'Loading' : 'Login'}
                      type='submit'
                      variant='success'
                      width='w-100'
                      onClick={handleLogin}
                    />
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
