import React from 'react'
import { useLocation, useNavigate } from 'react-router'

function OtherOverview() {
  const navigate = useNavigate()
  const location = useLocation();
  function test(){
    alert("")
  }

  return (
    <div style={{ display: 'flex', justifyContent: 'center', width: '1500px', border: '2px solid black', padding: '12px', margin: '10px', height: '100%' }}>
      {/* table */}
      <div className='container-fluid h-100'>

      <div className=''>
    <h1>Overview</h1>
    <br />

    <a href="thefile.pdf" download>
      <button>Download File</button>
    </a>
    <br />
    <br />
    <div>
      <input placeholder='comment section' style={{ height: '300px', width: '100%' }}></input>
      <br />
      <div style={{ float: 'right' }}>
        <button>Send</button>
      </div>


    </div>
  </div>
  </div>
  </div>
  )
}

export default OtherOverview