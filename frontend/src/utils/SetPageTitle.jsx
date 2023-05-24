export const SetPageTitle = (pathname) => {
  let pageTitle = ''
  // pasang switch untuk mengetahui title
  switch (pathname) {
    case '/':
      pageTitle = 'Home'
      break
    case '/profile':
      pageTitle = 'Profile'
      break
    case '/login':
      pageTitle = 'Login Page'
      break
    case '/register':
      pageTitle = 'Register Page'
      break

    default:
      pageTitle = 'GoBlog' // Judul default jika tidak ada yang cocok
  }

  document.title = `GoBlog - ${pageTitle}`
}
