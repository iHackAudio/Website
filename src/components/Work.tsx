import { useState, useCallback } from "react";
import "./styles/Work.css";
import WorkImage from "./WorkImage";
import { MdArrowBack, MdArrowForward } from "react-icons/md";

const projects = [
  {
    title: "ihack Audio Suite",
    category: "Audio Plugin Collection",
    tools: "VST3, AU, AAX, DSP, C++",
    image: "/images/project1.png",
    link: "https://ihackaudio.com",
  },
  {
    title: "Sound Design Portfolio",
    category: "Game & Film Audio",
    tools: "Wwise, FMOD, Pro Tools, Reaper",
    image: "/images/project2.png",
    link: "#",
  },
  {
    title: "Mixing & Mastering",
    category: "Music Production Service",
    tools: "Analog Hardware, Digital Processing",
    image: "/images/project3.png",
    link: "#",
  },
  {
    title: "Audio Tools API",
    category: "Developer Tools",
    tools: "JavaScript, Web Audio API, React",
    image: "/images/project4.png",
    link: "#",
  },
];

const Work = () => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isAnimating, setIsAnimating] = useState(false);

  const goToSlide = useCallback(
    (index: number) => {
      if (isAnimating) return;
      setIsAnimating(true);
      setCurrentIndex(index);
      setTimeout(() => setIsAnimating(false), 500);
    },
    [isAnimating]
  );

  const goToPrev = useCallback(() => {
    const newIndex =
      currentIndex === 0 ? projects.length - 1 : currentIndex - 1;
    goToSlide(newIndex);
  }, [currentIndex, goToSlide]);

  const goToNext = useCallback(() => {
    const newIndex =
      currentIndex === projects.length - 1 ? 0 : currentIndex + 1;
    goToSlide(newIndex);
  }, [currentIndex, goToSlide]);

  return (
    <div className="work-section section-container" id="work">
      <div className="work-container">
        <div className="work-header">
          <h2>
            Featured
            <br />
            <span>Projects</span>
          </h2>
          <div className="work-nav">
            <button
              onClick={goToPrev}
              className="work-nav-btn"
              disabled={isAnimating}
              aria-label="Previous project"
            >
              <MdArrowBack />
            </button>
            <button
              onClick={goToNext}
              className="work-nav-btn"
              disabled={isAnimating}
              aria-label="Next project"
            >
              <MdArrowForward />
            </button>
          </div>
        </div>

        <div className="work-slider">
          <div
            className="work-slider-track"
            style={{
              transform: `translateX(-${currentIndex * 100}%)`,
            }}
          >
            {projects.map((project, index) => (
              <div key={index} className="work-slide">
                <a
                  href={project.link}
                  target="_blank"
                  rel="noreferrer"
                  className="work-card"
                  data-cursor="disable"
                >
                  <div className="work-image-container">
                    <WorkImage
                      src={project.image}
                      alt={project.title}
                      className="work-image"
                    />
                  </div>
                  <div className="work-info">
                    <h3>{project.title}</h3>
                    <p className="work-category">{project.category}</p>
                    <p className="work-tools">{project.tools}</p>
                  </div>
                </a>
              </div>
            ))}
          </div>
        </div>

        <div className="work-dots">
          {projects.map((_, index) => (
            <button
              key={index}
              onClick={() => goToSlide(index)}
              className={`work-dot ${index === currentIndex ? "active" : ""}`}
              aria-label={`Go to project ${index + 1}`}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Work;
