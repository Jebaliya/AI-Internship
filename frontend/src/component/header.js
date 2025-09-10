import React from "react";
import "../styles.css";
import MCA from "../MCA.png";

function Header() {
  return (
    <header className="header">
      {/* Top bar */}
      <div className="top-bar">
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Flag_of_India.svg"
          alt="India Flag"
          className="flag"
        />
        <span>भारत सरकार / Government Of India</span>
        <div className="right-options">
          <span>English</span>
          <span>Screen Reader</span>
          <span>A- A A+</span>
        </div>
      </div>

      {/* Main header */}
      <div className="main-header">
        <img src={MCA} alt="MCA Logo" className="logo" />
        <img
          src="https://pminternship.gov.in/images/pm-internship-logo.png"
          alt="PM Internship"
          className="logo"
        />
        <div className="header-buttons">
          <button className="btn">Youth Registration</button>
          <button className="btn">Login</button>
        </div>
      </div>

      {/* Navigation menu */}
      <nav className="nav-bar">
        <a href="/">Home</a>
        <a href="/">Guidelines/Documentations</a>
        <a href="/">Gallery</a>
        <a href="/">Eligibility</a>
        <a href="/">Mobile App</a>
        <a href="/">Support</a>
        <a href="/">Compendium</a>
      </nav>
    </header>
  );
}

export default Header;
