import React from 'react';

const avatar = ({ width, height, ...rest }) => {
  return (
    <div>
      <img style={{ width, height }} {...rest} />
    </div>
  )
}

export default avatar;
