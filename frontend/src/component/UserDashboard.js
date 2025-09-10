import React, { useState } from "react";

function UserDashboard({
  user,
  name,
  setName,
  education,
  setEducation,
  skillsText,
  setSkillsText,
  interestsText,
  setInterestsText,
  location,
  setLocation,
  handleLogout,
  handleSubmit,
  recs,
  handleApply,
  resumeUrl,
}) {
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

        <form onSubmit={handleSubmit} className="form">
          <input
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Full name (optional)"
            required
          />
          <input
            value={education}
            onChange={(e) => setEducation(e.target.value)}
            placeholder="Education (e.g. B.Tech - Computer Engg)"
            required
          />
          <input
            value={skillsText}
            onChange={(e) => setSkillsText(e.target.value)}
            placeholder="Skills (comma separated) e.g. Python, SQL"
            required
          />
          <input
            value={interestsText}
            onChange={(e) => setInterestsText(e.target.value)}
            placeholder="Interests (comma separated) e.g. Data, Transport"
            required
          />
          <input
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            placeholder="Preferred location e.g. Gujarat"
            required
          />
          <button type="submit">Get Recommendations</button>
        </form>

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

export default UserDashboard;