import React, { useState } from 'react'
import Button from '../components/Button'
import Gap from '../components/Gap'
import Input from '../components/Input'
import ImageRegister from '../assets/images/auth.jpg'
import '../style/index.css'
import Particle from '../components/Particles.BG'
import { useNavigate } from 'react-router-dom'
import { registerUser } from '../services/Auth'
import { toast } from 'react-toastify'

const Register = () => {
  // deklarasi hooks register
  const [register, setRegister] = useState({
    name: '',
    email: '',
    password: '',
  })
  // animation loading
  const [loading, setLoading] = useState(false)
  // pasang use navigate
  const navigate = useNavigate()

  // handleChangeInput
  const handleChangeInput = (e) => {
    const { name, value } = e.target
    setRegister({ ...register, [name]: value })
  }
  // handleRegister
  const handleRegister = async (e) => {
    e.preventDefault()
    setLoading(true)
    try {
      const response = await registerUser(register)
      console.log(response.data)
      toast.success('Register Berhasil')
      setLoading(false)
      navigate('/login')
    } catch (error) {
      console.log(error.response.data)
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
                  src={ImageRegister}
                  className='img-fluid rounded'
                  style={{}}
                />
              </div>
              <div className='col-md-4 d-flex align-items-center'>
                <div className='card-body me-4'>
                  <form onSubmit={handleRegister}>
                    <h2 className='text-center'>Register </h2>
                    <Input
                      label='Username'
                      placeholder='Enter Username'
                      type='text'
                      name='username'
                      value={register.username}
                      onChange={handleChangeInput}
                    />
                    <Gap height={18} />
                    <Input
                      label='Email'
                      placeholder='Enter Email'
                      name='email'
                      type='email'
                      value={register.email}
                      onChange={handleChangeInput}
                    />
                    <Gap height={18} />
                    <Input
                      label='Password'
                      placeholder='Enter Password'
                      name='password'
                      type='password'
                      value={register.password}
                      onChange={handleChangeInput}
                    />
                    <Gap height={18} />
                    <Button
                      label={loading ? 'Loading' : 'Register'}
                      variant='success'
                      width='w-100'
                      disabled={loading}
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

export default Register
