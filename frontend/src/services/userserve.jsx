import axios from 'axios'
import { toast } from 'react-toastify'

// const API_URL = 'http://192.168.1.62:5000'

export const EditProfile = async (username, password) => {
  try {
    const response = await axios.patch(
      `${API_URL}/update/profile/<id>`,
      username,
      password
    )
    return response.data
  } catch (error) {
    throw error.response.data
  }
}

export const DeleteUser = async (username, password, email) => {
  try {
    const response = await axios.delete(
      `${API_URL}/update/profile/<id>`,
      username,
      password,
      email
    )
    return response.data
  } catch (error) {
    throw error.response.data
  }
}
