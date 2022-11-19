import React from 'react'
import './UploadButton.css'

function UploadButton(props) {
    return(
        <button className="upload-button">{props.text}</button>

    );
} 

export default UploadButton;