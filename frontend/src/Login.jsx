import React, { useState } from "react";
import axios from "axios";

const API_URL =
  process.env.REACT_APP_API_URL ||
  "https://ai-course-builder-1-smgs.onrender.com";

function Login({ setToken, onSwitch }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const login = async () => {
    setError("");

    try {
      const res = await axios.post(`${API_URL}/auth/login`, {
        email,
        password,
      });

      localStorage.setItem("token", res.data.access_token);
      setToken(res.data.access_token);
    } catch (err) {
      if (err.response?.data?.detail) {
        setError(err.response.data.detail);
      } else {
        setError("❌ Invalid credentials");
      }
    }
  };

  return (
    <div className="auth-box">
      <h2>Login</h2>

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

      <button onClick={login}>Login</button>

      {error && <p className="error">{error}</p>}

      <p className="link" onClick={onSwitch}>
        Create an account
      </p>
    </div>
  );
}

export default Login;
