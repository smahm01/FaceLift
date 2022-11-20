import React, { useState } from "react";
import './App.css'
import axios from 'axios';
  
function App() {
 
    const [file, setFile] = useState();

    function handleChange(e) {
        console.log(e.target.files);
        setFile(URL.createObjectURL(e.target.files[0]));
    }

    function uploadFile(e) {
      const formData = new FormData();   
      formData.append('image', e.target.files[0])
      fetch('http://localhost:3000/url_route', {
      method: 'POST',
      headers: { 'Content-Type': 'multipart/form-data' },
      body: formData
     })
    }

    
    
  
    return (
        <div className="App">
            <h2 className = "instruction-title">Welcome to FaceLift</h2>
            <h3 className = "instruction-subtitle">A targeted face blur technology meant to protect your privacy in an ever evolving technological world</h3>
            <h4 className = "instruction-description" >Upload images of those you don't want blurred</h4>
            <input className="input-button" type="file" onChange={uploadFile} />
            <button onClick={uploadFile} className ="upload-button"> Recognize!</button>
            <img className ="displayed-image" src={file} />
  
        </div>
  
    );
}
  
export default App;