import axios from 'axios'

const API_URL = 'http://192.168.1.62:5000'

export const article = async (title, content) => {
  try {
    const response = await axios.post(`${API_URL}/create/article`, title, content)
    return response.data
  } catch (error) {
    throw error.response.data
  }
}

