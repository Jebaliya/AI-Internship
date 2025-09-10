import React from "react";
import "../styles.css";

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-top">
        {/* Left Logos */}
        <div className="footer-logos">
          <img
            src="https://mca.gov.in/content/dam/mca/images/mca_logo.png"
            alt="Ministry of Corporate Affairs"
            className="footer-logo"
          />
          <img
            src="https://bisag-n.in/images/bisag-n.png"
            alt="BISAG-N"
            className="footer-logo"
          />
        </div>

        {/* Links */}
        <div className="footer-links">
          <h3>Get to Know</h3>
          <a href="#partners">Partner Companies</a>
          <a href="#guidelines">Guidelines</a>
          <a href="#faqs">FAQs</a>
          <a href="#manuals">Manuals</a>
          <a href="#videos">Videos</a>
          <a href="#privacy">Privacy Policy</a>
        </div>

        {/* Contact */}
        <div className="footer-contact">
          <h3>Contact Us</h3>
          <p>
            A Wing, 5th Floor, Shastri Bhawan,
            <br />
            Dr Rajendra Prasad Rd, New Delhi - 110001
          </p>
          <p>Email: pminternship[at]mca.gov.in</p>
          <p>Helpline: 1800 11 6090</p>
        </div>
      </div>

      <div className="footer-bottom">
        <p>
          © 2024 PM-INTERNSHIP, All Rights Reserved.
          <br />
          Site owned by Ministry of Corporate Affairs.
          <br />
          Technical collaboration with BISAG-N
        </p>
        <p className="visitors">Visitors: 4,13,77,960</p>
      </div>
    </footer>
  );
}
