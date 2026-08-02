import { MdArrowOutward, MdCopyright } from "react-icons/md";
import "./styles/Contact.css";

const Contact = () => {
  return (
    <div className="contact-section section-container" id="contact">
      <div className="contact-container">
        <h3>Contact</h3>
        <div className="contact-flex">
          <div className="contact-box">
            <h4>Connect</h4>
            <p>
              <a
                href="https://www.linkedin.com/in/yourprofile"
                target="_blank"
                rel="noreferrer"
                data-cursor="disable"
              >
                LinkedIn — yourprofile
              </a>
            </p>
            <p>
              <a
                href="mailto:hello@ihackaudio.com"
                data-cursor="disable"
              >
                hello@ihackaudio.com
              </a>
            </p>
            <h4>Location</h4>
            <p>Your City, Country</p>
          </div>
          <div className="contact-box">
            <h4>Social</h4>
            <a
              href="https://github.com/yourusername"
              target="_blank"
              rel="noreferrer"
              data-cursor="disable"
              className="contact-social"
            >
              GitHub
              <MdArrowOutward />
            </a>
            <a
              href="https://www.linkedin.com/in/yourprofile"
              target="_blank"
              rel="noreferrer"
              data-cursor="disable"
              className="contact-social"
            >
              LinkedIn
              <MdArrowOutward />
            </a>
            <a
              href="https://www.youtube.com/@yourchannel"
              target="_blank"
              rel="noreferrer"
              data-cursor="disable"
              className="contact-social"
            >
              YouTube
              <MdArrowOutward />
            </a>
            <a
              href="https://www.instagram.com/yourhandle"
              target="_blank"
              rel="noreferrer"
              data-cursor="disable"
              className="contact-social"
            >
              Instagram
              <MdArrowOutward />
            </a>
            <a
              href="https://twitter.com/yourhandle"
              target="_blank"
              rel="noreferrer"
              data-cursor="disable"
              className="contact-social"
            >
              Twitter/X
              <MdArrowOutward />
            </a>
          </div>
        </div>
        <div className="contact-footer">
          <p>
            <MdCopyright /> {new Date().getFullYear()} ihack Audio. All rights reserved.
          </p>
          <p>
            Designed with passion for sound
          </p>
        </div>
      </div>
    </div>
  );
};

export default Contact;
