import React, { useState } from "react";

const API_BASE = process.env.REACT_APP_API || "http://localhost:5000";

function App() {
  const [name, setName] = useState("");
  const [skillsText, setSkillsText] = useState("");
  const [education, setEducation] = useState("");
  const [interestsText, setInterestsText] = useState("");
  const [location, setLocation] = useState("");
  const [recs, setRecs] = useState([]);

  async function handleSubmit(e) {
    e.preventDefault();
    const skills = skillsText
      .split(",")
      .map((s) => s.trim())
      .filter(Boolean);
    const interests = interestsText
      .split(",")
      .map((s) => s.trim())
      .filter(Boolean);
    const preferred_locations = location ? [location] : [];

    const body = { skills, education, interests, preferred_locations };

    const res = await fetch(`${API_BASE}/api/recommend`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    const js = await res.json();
    setRecs(js.recommendations || []);
  }

  return (
    <div className="container">
      <header>
        <h1>AI Internship Recommender</h1>
        <p>Get 3–5 personalised internships</p>
      </header>

      <form onSubmit={handleSubmit} className="form">
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Full name (optional)"
        />
        <input
          value={education}
          onChange={(e) => setEducation(e.target.value)}
          placeholder="Education (e.g. B.Tech - Computer Engg)"
        />
        <input
          value={skillsText}
          onChange={(e) => setSkillsText(e.target.value)}
          placeholder="Skills (comma separated) e.g. Python, SQL"
        />
        <input
          value={interestsText}
          onChange={(e) => setInterestsText(e.target.value)}
          placeholder="Interests (comma separated) e.g. Data, Transport"
        />
        <input
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          placeholder="Preferred location e.g. Gujarat"
        />
        <button type="submit">Get Recommendations</button>
      </form>

      <section className="results">
        {recs.map((r, idx) => (
          <div className="card" key={idx}>
            <h3>
              {r.internship.title} — {r.internship.org}
            </h3>
            <p>Score: {r.score}</p>
            <p>
              <strong>Matched skills:</strong>{" "}
              {(r.matched_skills || []).join(", ") || "—"}
            </p>
            <p>{r.internship.description}</p>
            <p>
              <strong>Location:</strong> {r.internship.location} |{" "}
              <strong>Stipend:</strong> {r.internship.stipend}
            </p>
            <a href="#">Apply</a>
          </div>
        ))}
      </section>
    </div>
  );
}

export default App;

// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
