import "./styles/Career.css";

const Career = () => {
  return (
    <div className="career-section section-container">
      <div className="career-container">
        <h2>
          My career
          <span>&</span>
          <br />
          experience
        </h2>
        <div className="career-info">
          <div className="career-timeline">
            <div className="career-dot"></div>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Founder & CEO</h4>
                <h5>ihack Audio</h5>
              </div>
              <h3>NOW</h3>
            </div>
            <p>
              Leading ihack Audio, developing innovative audio solutions, plugins, 
              and sound design tools for music producers, filmmakers, and game developers. 
              Building a community of audio enthusiasts and delivering premium audio experiences.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Senior Audio Engineer</h4>
                <h5>Studio Name · Location</h5>
              </div>
              <h3>2020–2024</h3>
            </div>
            <p>
              Mixed and mastered tracks for major label artists, developed custom 
              audio processing chains, and led a team of engineers in delivering 
              high-quality audio productions across multiple genres.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Sound Designer</h4>
                <h5>Previous Company</h5>
              </div>
              <h3>2017–2020</h3>
            </div>
            <p>
              Created original sound design for video games, films, and commercials. 
              Developed audio libraries and implemented interactive audio systems 
              using Wwise and FMOD.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Audio Engineering Degree</h4>
                <h5>University/Institution</h5>
              </div>
              <h3>2013–2017</h3>
            </div>
            <p>
              Bachelor's degree in Audio Engineering with focus on digital signal 
              processing, acoustics, and music production technology.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Career;
