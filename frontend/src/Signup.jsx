import React, { useState } from "react";
import axios from "axios";

const API_URL =
  process.env.REACT_APP_API_URL ||
  "https://ai-course-builder-1-smgs.onrender.com";

function Signup({ onSwitch }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState("");

  const signup = async () => {
    setMsg("");
    try {
      await axios.post(`${API_URL}/auth/signup`, {
        email,
        password,
      });
      setMsg("✅ Signup successful. Please login.");
    } catch (err) {
      setMsg(err.response?.data?.detail || "❌ Signup failed");
    }
  };

  return (
    <div className="auth-box">
      <h2>Signup</h2>

      <input
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button onClick={signup}>Signup</button>

      {msg && <p>{msg}</p>}

      <p className="link" onClick={onSwitch}>
        Back to login
      </p>
    </div>
  );
}

export default Signup;
