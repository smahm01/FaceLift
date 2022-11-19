import React from 'react'
import './Navbar.css'
import logo from './/logo/logo-removebg-preview.png';


function Navbar() {
    return(
        <nav className="navbar">
            <img src={logo} alt = "upload"/>
        </nav>

    );
} 

export default Navbar;