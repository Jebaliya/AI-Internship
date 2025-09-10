import React, { useState } from "react";

function Register({ apiBase }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");
  const [resumeFile, setResumeFile] = useState(null);
  const [msg, setMsg] = useState("");
  const [isAdmin, setIsAdmin] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    const formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);
    formData.append("confirm", confirm);
    formData.append("is_admin", isAdmin ? "true" : "false");
    if (resumeFile) formData.append("resume", resumeFile);

    const res = await fetch(`${apiBase}/api/register`, {
      method: "POST",
      body: formData,
    });
    const js = await res.json();
    if (js.status === "registered") {
      window.alert("Registration successful! Please login.");
      window.location.href = "/login";
    } else {
      setMsg(js.error || "Registration failed.");
    }
  }

  return (
    <form onSubmit={handleSubmit} className="form">
      <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" required />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" required />
      <input type="password" value={confirm} onChange={e => setConfirm(e.target.value)} placeholder="Confirm Password" required />
      <input type="file" accept=".pdf,.doc,.docx" onChange={e => setResumeFile(e.target.files[0])} />
      <div className="admin-checkbox-row">
        <input
          type="checkbox"
          id="admin-checkbox"
          checked={isAdmin}
          onChange={e => setIsAdmin(e.target.checked)}
          className="admin-checkbox"
        />
        <label htmlFor="admin-checkbox" className="admin-checkbox-label">
          Register as Admin
        </label>
      </div>
      <button type="submit">Register</button>
      {msg && <p>{msg}</p>}
    </form>
  );
}

export default Register;