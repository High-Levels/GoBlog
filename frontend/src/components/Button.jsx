import React from 'react';

const Button = ({ label, variant, width, ...rest }) => {
  return (
    <div>
      <button {...rest} className={`btn btn-${variant} ${width}`}>
        {label}
      </button>
    </div>
  )
}

export default Button;
