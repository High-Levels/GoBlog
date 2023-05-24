import axios from 'axios'

// const API_URL = 'http://localhost:5000'
const API_URL = '/api/blog'

export const registerUser = async (userData) => {
  try {
    const response = await axios.post(`${API_URL}/register`, userData, {
      headers: { 'Content-Type': 'application/json' },
    })
    return response.data
  } catch (error) {
    throw error.response.data
  }
}

export const login = async (username, password) => {
  try {
    const response = await axios.post(`${API_URL}/login`, {
      username,
      password,
    })

    const { accessToken, refreshToken } = response.data

    localStorage.setItem('accessToken', accessToken)
    localStorage.setItem('refreshToken', refreshToken)

    return response.data
  } catch (error) {
    throw new Error(error.response.data.Message)
  }
}
