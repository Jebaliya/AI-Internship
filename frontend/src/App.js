import React, { useState, useEffect } from "react";
import "./styles.css"; // Ensure styles are imported
import Register from "./component/Register";
import Login from "./component/Login";

const API_BASE = process.env.REACT_APP_API || "http://localhost:5000";

function App() {
  const [name, setName] = useState("");
  const [skillsText, setSkillsText] = useState("");
  const [education, setEducation] = useState("");
  const [interestsText, setInterestsText] = useState("");
  const [location, setLocation] = useState("");
  const [recs, setRecs] = useState([]);
  const [resumeFile, setResumeFile] = useState(null);
  const [resumePreview, setResumePreview] = useState(null);
  const [jwt, setJwt] = useState(localStorage.getItem("jwt") || "");
  const [user, setUser] = useState(null);
  const [page, setPage] = useState("main"); // "main", "login", "register"

  function handleLogin(token, userData) {
    setJwt(token);
    setUser(userData);
    localStorage.setItem("jwt", token);
    setPage("main");
  }

  function handleLogout() {
    setJwt("");
    setUser(null);
    localStorage.removeItem("jwt");
    setPage("login");
  }

  useEffect(() => {
    if (!jwt) setPage("login");
  }, [jwt]);

  useEffect(() => {
    if (jwt && !user) {
      fetch(`${API_BASE}/api/me`, {
        headers: { Authorization: `Bearer ${jwt}` },
      })
        .then((res) => (res.ok ? res.json() : null))
        .then((data) => {
          if (data && data.user) setUser(data.user);
        });
    }
  }, [jwt, user]);

  useEffect(() => {
    if (user) {
      setName(user.name || "");
      setEducation(user.education || "");
      setSkillsText((user.skills || []).join(", "));
      setInterestsText((user.interests || []).join(", "));
      setLocation(
        (user.preferred_locations && user.preferred_locations[0]) || ""
      );
    }
  }, [user]);

  async function handleResumeChange(e) {
    const file = e.target.files[0];
    setResumeFile(file);
    if (file) {
      setResumePreview(URL.createObjectURL(file));

      // Send file to backend for parsing
      const formData = new FormData();
      formData.append("resume", file);

      const res = await fetch(`${API_BASE}/api/parse_resume`, {
        method: "POST",
        body: formData,
      });
      if (res.ok) {
        const data = await res.json();
        // Fill fields with extracted data if available
        if (data.name) setName(data.name);
        if (data.education) setEducation(data.education);
        if (data.skills && data.skills.length)
          setSkillsText(data.skills.join(", "));
        if (data.interests && data.interests.length)
          setInterestsText(data.interests.join(", "));
        if (data.location) setLocation(data.location);
      }
    } else {
      setResumePreview(null);
    }
  }

  async function handleSubmit(e) {
    e.preventDefault();
    if (!name || !education || !skillsText || !interestsText || !location) {
      alert("Please fill all fields before submitting.");
      return;
    }
    const skills = skillsText
      .split(",")
      .map((s) => s.trim())
      .filter(Boolean);
    const interests = interestsText
      .split(",")
      .map((s) => s.trim())
      .filter(Boolean);
    const preferred_locations = location ? [location] : [];

    // Send JSON, not FormData
    const body = {
      skills,
      education,
      interests,
      preferred_locations,
    };

    const res = await fetch(`${API_BASE}/api/recommend`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    const js = await res.json();
    setRecs(js.recommendations || []);
  }

  async function handleApply(internship) {
    if (window.confirm("Are you sure to Apply?")) {
      const skills = skillsText
        .split(",")
        .map((s) => s.trim())
        .filter(Boolean);
      const interests = interestsText
        .split(",")
        .map((s) => s.trim())
        .filter(Boolean);
      const preferred_locations = location ? [location] : [];
      const application = {
        name,
        education,
        skills,
        interests,
        preferred_locations,
        internship_id: internship.id,
      };
      // Optionally send resume with application
      const formData = new FormData();
      Object.entries(application).forEach(([k, v]) => {
        formData.append(k, typeof v === "object" ? JSON.stringify(v) : v);
      });
      if (resumeFile) formData.append("resume", resumeFile);

      const res = await fetch(`${API_BASE}/api/apply`, {
        method: "POST",
        body: formData,
      });
      if (res.ok) {
        alert("Application submitted successfully!");
      } else {
        alert("Failed to submit application.");
      }
    }
  }

  const resumeUrl = user && user.email
    ? `${API_BASE}/api/resume/${user.email}`
    : null;

  if (page === "register") {
    return (
      <div className="main-layout">
        <div className="container left-pane">
          <h2>Register</h2>
          <Register apiBase={API_BASE} />
          <button onClick={() => setPage("login")}>Go to Login</button>
        </div>
      </div>
    );
  }

  if (page === "login") {
    return (
      <div className="main-layout">
        <div className="container left-pane">
          <h2>Login</h2>
          <Login apiBase={API_BASE} onLogin={handleLogin} />
          <button onClick={() => setPage("register")}>Go to Register</button>
        </div>
      </div>
    );
  }

  return (
    <div className="main-layout">
      <div className="container left-pane">
        <header>
          <h1>AI Internship Recommender</h1>
          {user && (
            <div>
              <span>Welcome, {user.name || user.email}</span>
              <button onClick={handleLogout}>Logout</button>
            </div>
          )}
        </header>

<<<<<<< HEAD
        <form onSubmit={handleSubmit} className="form">
          <input
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Full name (optional)"
            required
          />
=======
      <form onSubmit={handleSubmit} className="form">
        <label>
          Name:
          <input
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Full name "
            required
          />
        </label>
        <label>
          Education:
>>>>>>> 751384f569368c10763a8b14adb12d713507917f
          <input
            value={education}
            onChange={(e) => setEducation(e.target.value)}
            placeholder="Education (e.g. B.Tech - Computer Engg)"
            required
          />
<<<<<<< HEAD
=======
        </label>
        <label>
          Skills:
>>>>>>> 751384f569368c10763a8b14adb12d713507917f
          <input
            value={skillsText}
            onChange={(e) => setSkillsText(e.target.value)}
            placeholder="Skills (comma separated) e.g. Python, SQL"
            required
          />
<<<<<<< HEAD
=======
        </label>
        <label>
          Interests:
>>>>>>> 751384f569368c10763a8b14adb12d713507917f
          <input
            value={interestsText}
            onChange={(e) => setInterestsText(e.target.value)}
            placeholder="Interests (comma separated) e.g. Data, Transport"
            required
          />
<<<<<<< HEAD
=======
        </label>
        <label>
          Preferred location:
>>>>>>> 751384f569368c10763a8b14adb12d713507917f
          <input
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            placeholder="Preferred location e.g. Gujarat"
            required
          />
<<<<<<< HEAD
          <button type="submit">Get Recommendations</button>
        </form>
=======
        </label>
        <button type="submit">Get Recommendations</button>
      </form>
>>>>>>> 751384f569368c10763a8b14adb12d713507917f

        <section className="results">
          {recs.map((r, idx) => (
            <div className="card" key={idx}>
              <h3>
                {r.internship.title} — {r.internship.org}
              </h3>
              {/* <p>Score: {r.score}</p> */}
              <p>
                <strong>Matched skills:</strong>{" "}
                {(r.matched_skills || []).join(", ") || "—"}
              </p>
              <p>{r.internship.description}</p>
              <p>
                <strong>Location:</strong> {r.internship.location} |{" "}
                <strong>Stipend:</strong> {r.internship.stipend}
              </p>
              <a href="#" onClick={() => handleApply(r.internship)}>
                Apply
              </a>
            </div>
          ))}
        </section>
      </div>
      <div className="resume-pane">
        <h2>Resume Preview</h2>
        {resumeUrl ? (
          <iframe
            src={resumeUrl}
            title="Resume Preview"
            className="resume-preview"
          />
        ) : (
          <div className="resume-placeholder">
            <p>No resume uploaded.</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;