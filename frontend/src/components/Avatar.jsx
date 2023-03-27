import React from 'react'

const avatar = ({ width, heigh, ...rest }) => {
  return (
    <div>
      <img style={{ width, heigh }} {...rest} />
    </div>
  )
}

export default avatar
