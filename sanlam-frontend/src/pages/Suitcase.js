import React, { useState } from 'react'
import '../Style.css'
import { useNavigate } from 'react-router-dom';
import Overview from './Overview';

const policy_data = [
  {
    i: 1, type: "Policy", name: 'Group Information and Data Policy', status: 'X', entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
    firstapproval: "", frequency: "", nextreview: "", version: "1.2", related: ""
  },
  {
    i: 2, type: "Policy", name: 'Group IT Policy', status: 'A', entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
    firstapproval: "", frequency: "", nextreview: "", version: "5.6", related: ""
  },
  {
    i: 3, type: "Policy", name: 'Group Cyber Security Policy', status: 'B', entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
    firstapproval: "", frequency: "", nextreview: "", version: "2.2", related: ""
  },
  {
    i: 4, type: "Policy", name: 'Group Digital Behaviour (User) Policy', status: 'B', entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
    firstapproval: "", frequency: "", nextreview: "", version: "3.7", related: ""
  }]

const standard_data = [
  {i: 1, type: "Standard", name: 'IT Governance', status: 'A', belongs: 2, entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 2, type: "Standard", name: 'Green IT', status: 'S', belongs: 2, entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 3, type: "Standard", name: 'Capacity Management', status: 'A', belongs: 2, entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 4, type: "Standard", name: 'Bus.Change, SDLC & Project Mgt', status: 'S', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 5, type: "Standard", name: 'IT Financial Management', status: 'I', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 6, type: "Standard", name: 'IT Management - generic', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 7, type: "Standard", name: 'Incident Management', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 8, type: "Standard", name: 'Problem Management', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 9, type: "Standard", name: 'Technology asset removal & disposal', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 10, type: "Standard", name: 'IT Risk Management', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 11, type: "Standard", name: 'Cloud / Technology Outsourcing', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 12, type: "Standard", name: 'Change Control', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 13, type: "Standard", name: 'Release and Deployment Mgt', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 14, type: "Standard", name: 'Supplier Management', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 15, type: "Standard", name: 'Internal capability improvement', status: 'X', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 16, type: "Standard", name: 'IT Continuity Management', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 17, type: "Standard", name: 'Mgt controls for enabling end-users', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 18, type: "Standard", name: 'Configuration Management', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 19, type: "Standard", name: 'IT-Due Diligence', status: 'X', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 20, type: "Standard", name: 'Architecture Management', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""}]

const guideline_data = [
  {i: 1, type: "Guideline", name: 'Cloud / Technology Outsourcing Implementation Guide', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 2, type: "Guideline", name: 'Guidelines: Other', status: 'X', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 3, type: "Guideline", name: 'Architecture Guiding Principles', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 4, type: "Guideline", name: 'IT Measurement', status: 'X', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""},
  {i: 5, type: "Guideline", name: 'IT Risk Management Guidelines', status: 'A', belongs: 2,  entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
  firstapproval: "", frequency: "", nextreview: "", version: "", related: ""}]

function Suitcase() {
  const [standards, setStandards] = useState([])
  const [guidelines, setGuidelines] = useState([])
  const [overview, setOverview] = useState([{
    name: 'Group Information and Data Policy', entities: "", governancearea: "", authority: "", sponsor: "", responsible: "",
    firstapproval: "", frequency: "",
    nextreview: "",
    version: "", related: ""
  }])
  const [active, setActive] = useState(1);
  const navigate = useNavigate()

  function a_clicked(a) {
    navigate('/overview', {state: {d: a.i, data: a}})
  }

  function b_clicked(a) {
    navigate('/otheroverview', {state: {d: a.i, data: a}})
  }

  function one(i) {
    setActive(i)
    const s = standard_data.filter(s => s.belongs === i)
    setStandards(s)
    const g = guideline_data.filter(g => g.belongs === i)
    setGuidelines(g)
    const o = policy_data.filter(o => o.i === i)
    setOverview(o)
  }

  const btntype = {
    A: 'p-btn btn-approved',
    X: 'p-btn btn-not_started',
    S: 'p-btn btn-starting',
    B: 'p-btn btn-being_developed',
    I: 'p-btn btn-in_sign_off'
  }

  const btncolor = {
    A: 't-btn-approved-active',
    X: 't-btn-not-started-active',
    S: 't-btn-starting-active',
    B: 't-btn-being-developed-active',
    I: 't-btn-in-sign-off-active'
  }

  const userType = "admin"


  const btnstatus = {
    A: 'top-left square-approved', X: "top-left square-not-started", S: "top-left square-starting", B: "top-left square-being-developed",
    I: "top-left square-in-sign-off"
  }
  return (
    <div style={{ display: 'flex', justifyContent: 'center', width: '1500px', border: '2px solid black', padding: '12px', margin: '10px', height: '100%' }}>
      {/* table */}
      <div className='container-fluid h-100'>
        {/* legend keys */}
        <div style={{ fontSize: '16px', margin: '10px', textAlign: 'center' }}>
          <div class="legend-not-started"><b>X</b></div> - Not Started
          <div class="legend-starting"><b>S</b></div> - Starting
          <div class="legend-being-developed"><b>B</b></div> - Being Developed
          <div class="legend-in-sign-off"><b>I</b></div> - In Sign Off
          <div class="legend-approved"><b>A</b></div> - Approved
        </div>

        {/* tabs */}
        <div class="row tab">
          <div class="col-sm-2 " style={{ fontSize: '30px' }}>Group Policies</div>

          {policy_data.map(u => <div class="col p-0"><button className={active === u.i ? 'active' : 'btn-secondary inactive'} onClick={() => one(u.i)}><button className={active === u.i ? btncolor[u.status] : 't-btn-inactive'}>{active === u.i && <div class={btnstatus[u.status]}><b>{u.status}</b></div>}{u.name}</button></button></div>)}


        </div>

        {/* group standards row */}
        <div class="row" style={{ backgroundColor: '#d3d3d3' }}>
          <div class="col-sm-2" style={{ fontSize: '30px' }}>Group Standards</div>
          <div class="col d-flex justify-content-between flex-wrap p-0">
            {standards.map((u) => (
              <button onClick={() => a_clicked(u)} title={u.name} class={btntype[u.status]}>{u.status !== "X" && <div class={btnstatus[u.status]}><b>{u.status}</b></div>}{u.name}</button>
            ))}
          </div>
        </div>

        {/* group guidelines row */}
        <div class="row" style={{ backgroundColor: '#f2f2f2' }}>
          <div class="col-sm-2" style={{ fontSize: '30px' }}>Group Guidelines</div>
          <div class="col d-flex justify-content-between flex-wrap p-0">
            {guidelines.map((u) => (
              <button onClick={() => b_clicked(u)} title={u.name} class={btntype[u.status]}>{u.status !== "X" && <div class={btnstatus[u.status]}><b>{u.status}</b></div>}{u.name}</button>
            ))}
          </div>
        </div>
        <br /><br /><br />
        <div className=''>
          <h1>Overview</h1>
          
          <br />
          {userType === "admin" && <button style={{float: "right"}}>Edit</button>}
          <table className='table table-bordered table-hover'>

            <tbody >

              <tr >
                <td>Type of Policy:</td>
                <td>{overview.map(u => u.name)}</td>
              </tr>
              <tr >
                <td>Sanlam Entities subject to this Policy:</td>
                <td>{overview.map(u => u.entities)}</td>
              </tr>
              <tr >
                <td>Governance Area Addressed:</td>
                <td>{overview.map(u => u.governancearea)}</td>
              </tr>
              <tr >
                <td>Approving Authority:</td>
                <td>{overview.map(u => u.authority)}</td>
              </tr>
              <tr >
                <td>Group ExCo Sponsor:</td>
                <td>{overview.map(u => u.sponsor)}</td>
              </tr>
              <tr >
                <td>Responsible Person:</td>
                <td>{overview.map(u => u.responsible)}</td>
              </tr>
              <tr >
                <td>Date of First Approval:</td>
                <td>{overview.map(u => u.firstapproval)}</td>
              </tr>
              <tr >
                <td>Frequency of Review or Update:</td>
                <td>{overview.map(u => u.frequency)}</td>
              </tr>
              <tr >
                <td>Date of Next Review:</td>
                <td>{overview.map(u => u.nextreview)}</td>
              </tr>
              <tr >
                <td>Version Number:</td>
                <td>{overview.map(u => u.version)}</td>
              </tr>
              <tr >
                <td>Related Policies:</td>
                <td>{overview.map(u => u.related)}</td>
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
    
  );
}

export default Suitcase