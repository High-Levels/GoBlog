import React from 'react'

const Button = ({ label, variant, ...rest }) => {
  return (
    <div>
      <button {...rest} className={`btn btn-${variant}`}>
        {label}
      </button>
    </div>
  )
}

export default Button
