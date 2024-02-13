import React from 'react'
import { useState } from 'react'

function AdminOverview() {
  const [file, setfile] = useState()
  function clickupload(e) {
    document.getElementById('real-upload-button').click()
  }
  return (
    <div className='container'>
      <h1>Overview</h1>
      <br />
      <table className='table table-bordered table-hover'>

        <tbody >
        <tr >
            <td>Type of Policy:</td>
            <td><input placeholder='original information goes here but if you click on it you can change it' maxLength='50' style={{border: 'none', width: '100%'}}/></td>
          </tr>
          <tr >
            <td>Sanlam Entities subject to this Policy:</td>
            <td><input placeholder='original information goes here but if you click on it you can change it' maxLength='50' style={{border: 'none', width: '100%'}}/></td>
          </tr>
          <tr >
            <td>Governance Area Addressed:</td>
            <td><input placeholder='original information goes here but if you click on it you can change it' maxLength='50' style={{border: 'none', width: '100%'}}/></td>
          </tr>
          <tr >
            <td>Approving Authority:</td>
            <td><input placeholder='original information goes here but if you click on it you can change it' maxLength='50' style={{border: 'none', width: '100%'}}/></td>
          </tr>
          <tr >
            <td>Group ExCo Sponsor:</td>
            <td><input placeholder='original information goes here but if you click on it you can change it' maxLength='50' style={{border: 'none', width: '100%'}}/></td>
          </tr>
          <tr >
            <td>Responsible Person:</td>
            <td><input placeholder='original information goes here but if you click on it you can change it' maxLength='50' style={{border: 'none', width: '100%'}}/></td>
          </tr>
          <tr >
            <td>Date of First Approval:</td>
            <td><input placeholder='original information goes here but if you click on it you can change it' maxLength='50' style={{border: 'none', width: '100%'}}/></td>
          </tr>
          <tr >
            <td>Frequency of Review or Update:</td>
            <td><input placeholder='original information goes here but if you click on it you can change it' maxLength='50' style={{border: 'none', width: '100%'}}/></td>
          </tr>
          <tr >
            <td>Date of Next Review:</td>
            <td><input placeholder='original information goes here but if you click on it you can change it' maxLength='50' style={{border: 'none', width: '100%'}}/></td>
          </tr>
          <tr >
            <td>Version Number:</td>
            <td><input placeholder='original information goes here but if you click on it you can change it' maxLength='50' style={{border: 'none', width: '100%'}}/></td>
          </tr>
          <tr >
            <td>Related Policies:</td>
            <td><input placeholder='original information goes here but if you click on it you can change it' maxLength='50' style={{border: 'none', width: '100%'}}/></td>
          </tr>

        </tbody>

      </table>

      <br />
      <br />
      <div>
        <input type='file' hidden='hidden' id='real-upload-button'/>
        <button type='button' onClick={clickupload}>Upload Button</button>
        <span>{file !== "" && "No file selected"}</span>

        <br />
        <div style={{ float: 'right' }}>
          <button>Submit</button>
        </div>

      </div>
    </div>
  )
}

export default AdminOverview