import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'
import Navbar from './Navbar';
import App from './App'
import background from './/logo/gradient-hexagonal-background_23-2148952241.png';




const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <><Navbar />
    <div style={{ backgroundImage: `url(${background})` }} >
    <App />
    </div></>

);
