import React from 'react'
import { useLocation, useNavigate } from 'react-router'

function Overview() {
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
    <table className='table table-bordered table-hover'>

      <tbody >

        <tr >
          <td>Type of Policy:</td>
          <td>{location.state.data.name}</td>
        </tr>
        <tr>
          <td>Sanlam Entities subject to this Policy:</td>
          <td>{location.state.data.entities}</td>
        </tr>
        <tr >
          <td>Governance Area Addressed:</td>
          <td>{location.state.data.governancearea}</td>
        </tr>
        <tr >
          <td>Approving Authority:</td>
          <td>{location.state.data.authority}</td>
        </tr>
        <tr >
          <td>Group ExCo Sponsor:</td>
          <td>{location.state.data.sponsor}</td>
        </tr>
        <tr >
          <td>Responsible Person:</td>
          <td>{location.state.data.responsible}</td>
        </tr>
        <tr >
          <td>Date of First Approval:</td>
          <td>{location.state.data.firstapproval}</td>
        </tr>
        <tr >
          <td>Frequency of Review or Update:</td>
          <td>{location.state.data.frequency}</td>
        </tr>
        <tr >
          <td>Date of Next Review:</td>
          <td>{location.state.data.nextreview}</td>
        </tr>
        <tr >
          <td>Version Number:</td>
          <td>{location.state.data.version}</td>
        </tr>
        <tr >
          <td>Related Policies:</td>
          <td>{location.state.data.related}</td>
        </tr>

      </tbody>

    </table>
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

export default Overview