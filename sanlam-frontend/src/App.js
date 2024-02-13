import Suitcase from './pages/Suitcase';
import Overview from './pages/Overview';
import AdminOverview from './pages/AdminOverview'
import React from "react";
import {BrowserRouter,Routes,Route} from "react-router-dom";
import OtherOverview from './pages/OtherOverview';
  
function App() {
    
  return (
      <>
      <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<Suitcase/>}/>
        <Route exact path="/overview" element={<Overview/>}/>
        <Route exact path="/adminoverview" element={<AdminOverview/>}/>
        <Route exact path="/otheroverview" element={<OtherOverview/>}/>
      </Routes>
      </BrowserRouter>
      </>
  );
}

export default App;
