import React, { useState } from "react";
import UploadButton from './UploadButton'
import './App.css'
import axios from 'axios';
  
function App() {
    const [file, setFile] = useState();

    function handleChange(e) {
        console.log(e.target.files);
        setFile(URL.createObjectURL(e.target.files[0]));
    }

    
    function handleSubmit(event) {
      event.preventDefault()
      console.log("hello world");
      const url = 'http://localhost:3000/url_route';
      const formData = new FormData();
      formData.append('file', file);
      const config = {
        headers: {
          'content-type': 'multipart/form-data',
        },
      };
      axios.post(url, formData, config).then((response) => {
        console.log(response.data);
      });
  
    }
    
  
    return (
        <div className="App">
            <h2 className = "instruction-title">Upload images </h2>
            <h4 className = "instruction-description" >Upload images of those you don't want blurred</h4>
            <input className="input-button" type="file" onChange={handleChange} />
            <UploadButton onSubmit={handleSubmit} text="Recognize!" className =".upload-button"/>
            <img className ="displayed-image" src={file} />
  
        </div>
  
    );
}
  
export default App;