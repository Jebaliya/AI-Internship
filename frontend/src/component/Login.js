import React, { useState } from "react";

function Login({ apiBase, onLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    const res = await fetch(`${apiBase}/api/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    const js = await res.json();
    if (js.token) {
      onLogin(js.token, js.user);
      setMsg("Login successful!");
    } else {
      setMsg(js.error || "Login failed.");
    }
  }

  return (
    <form onSubmit={handleSubmit} className="form">
      <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" required />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" required />
      <button type="submit">Login</button>
      {msg && <p>{msg}</p>}
    </form>
  );
}

export default Login;