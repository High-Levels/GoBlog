import React from 'react';
// import Modal from '../../components/Modal';
import Profile from './Profile';
import { EditProfile } from '../../services/userserve';
import { useNavigate } from 'react-router-dom';

export const Account = () => {
  const navigate = useNavigate()
  const handleprofilechange = async (e) => {
    e.preventDefault()
    setIsLoading(true)

    try {
      await EditProfile(username, password)
      toast.success('Akun berhasil diubah')
      setIsLoading(false)
      navigate('/profile')
    } catch (error) {
      setIsLoading(false)
      setError(error.message)
    }
  }
  return (
    <div>
      <Profile />
    </div>
  )
}
