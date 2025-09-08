import React, { useState } from "react";

function ApplyForm({ onSubmit, apiBase }) {
  const [name, setName] = useState("");
  const [skillsText, setSkillsText] = useState("");
  const [education, setEducation] = useState("");
  const [interestsText, setInterestsText] = useState("");
  const [location, setLocation] = useState("");
  const [resumeFile, setResumeFile] = useState(null);

  async function handleResumeUpload(e) {
    const file = e.target.files[0];
    setResumeFile(file);

    if (!file) return;

    const formData = new FormData();
    formData.append("resume", file);

    const res = await fetch(`${apiBase}/api/extract_resume`, {
      method: "POST",
      body: formData,
    });
    const js = await res.json();

    if (js.name) setName(js.name);
    if (js.skills) setSkillsText(js.skills.join(", "));
    if (js.education) setEducation(js.education);
    if (js.interests) setInterestsText(js.interests.join(", "));
    if (js.location) setLocation(js.location);
  }

  function handleSubmit(e) {
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
    onSubmit(body);
  }

  return (
    <form onSubmit={handleSubmit} className="form">
      <input
        type="file"
        accept=".pdf,.doc,.docx"
        onChange={handleResumeUpload}
        style={{ marginBottom: "1em" }}
      />
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
  );
}

export default ApplyForm;
