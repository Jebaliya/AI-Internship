import React, { useEffect, useState } from "react";

function AdminDashboard({ apiBase, jwt }) {
  const [internships, setInternships] = useState([]);
  const [applications, setApplications] = useState([]);
  const [form, setForm] = useState({
    title: "",
    org: "",
    description: "",
    required_skills: "",
    sector: "",
    location: "",
    stipend: "",
    duration: "",
  });
  const [editId, setEditId] = useState(null);

  useEffect(() => {
    fetch(`${apiBase}/api/admin/internships`, {
      headers: { Authorization: `Bearer ${jwt}` }
    })
      .then(res => res.json())
      .then(setInternships);

    fetch(`${apiBase}/api/admin/applications`, {
      headers: { Authorization: `Bearer ${jwt}` }
    })
      .then(res => res.json())
      .then(setApplications);
  }, [apiBase, jwt]);

  function handleFormChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  function handleAdd(e) {
    e.preventDefault();
    const data = {
      ...form,
      required_skills: form.required_skills.split(",").map(s => s.trim()).filter(Boolean),
    };
    fetch(`${apiBase}/api/admin/internships`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${jwt}`
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(() => {
        setForm({
          title: "",
          org: "",
          description: "",
          required_skills: "",
          sector: "",
          location: "",
          stipend: "",
          duration: "",
        });
        // Refresh internships
        fetch(`${apiBase}/api/admin/internships`, {
          headers: { Authorization: `Bearer ${jwt}` }
        })
          .then(res => res.json())
          .then(setInternships);
      });
  }

  function handleEdit(i) {
    setEditId(i.id);
    setForm({
      title: i.title,
      org: i.org,
      description: i.description,
      required_skills: (i.required_skills || []).join(", "),
      sector: i.sector,
      location: i.location,
      stipend: i.stipend,
      duration: i.duration,
    });
  }

  function handleUpdate(e) {
    e.preventDefault();
    const data = {
      ...form,
      required_skills: form.required_skills.split(",").map(s => s.trim()).filter(Boolean),
    };
    fetch(`${apiBase}/api/admin/internships/${editId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${jwt}`
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(() => {
        setEditId(null);
        setForm({
          title: "",
          org: "",
          description: "",
          required_skills: "",
          sector: "",
          location: "",
          stipend: "",
          duration: "",
        });
        fetch(`${apiBase}/api/admin/internships`, {
          headers: { Authorization: `Bearer ${jwt}` }
        })
          .then(res => res.json())
          .then(setInternships);
      });
  }

  function handleDelete(id) {
    if (window.confirm("Delete this internship?")) {
      fetch(`${apiBase}/api/admin/internships/${id}`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${jwt}` }
      })
        .then(res => res.json())
        .then(() => {
          fetch(`${apiBase}/api/admin/internships`, {
            headers: { Authorization: `Bearer ${jwt}` }
          })
            .then(res => res.json())
            .then(setInternships);
        });
    }
  }

  return (
    <div>
      <h2>Internships</h2>
      <form onSubmit={editId ? handleUpdate : handleAdd} style={{ marginBottom: "2em" }}>
        <input name="title" value={form.title} onChange={handleFormChange} placeholder="Title" required />
        <input name="org" value={form.org} onChange={handleFormChange} placeholder="Organization" required />
        <input name="description" value={form.description} onChange={handleFormChange} placeholder="Description" required />
        <input name="required_skills" value={form.required_skills} onChange={handleFormChange} placeholder="Required Skills (comma separated)" required />
        <input name="sector" value={form.sector} onChange={handleFormChange} placeholder="Sector" required />
        <input name="location" value={form.location} onChange={handleFormChange} placeholder="Location" required />
        <input name="stipend" value={form.stipend} onChange={handleFormChange} placeholder="Stipend" required />
        <input name="duration" value={form.duration} onChange={handleFormChange} placeholder="Duration" required />
        <button type="submit">{editId ? "Update Internship" : "Add Internship"}</button>
        {editId && <button type="button" onClick={() => { setEditId(null); setForm({ title: "", org: "", description: "", required_skills: "", sector: "", location: "", stipend: "", duration: "" }); }}>Cancel</button>}
      </form>
      <ul>
        {internships.map(i => (
          <li key={i.id}>
            {i.title} - {i.org} ({i.location})
            <button onClick={() => handleEdit(i)} style={{ marginLeft: "1em" }}>Edit</button>
            <button onClick={() => handleDelete(i.id)} style={{ marginLeft: "0.5em" }}>Delete</button>
          </li>
        ))}
      </ul>
      <h2>Applications</h2>
      <ul>
        {applications.map(a => (
          <li key={a.id}>{a.name} applied for {a.internship_id}</li>
        ))}
      </ul>
    </div>
  );
}

export default AdminDashboard;