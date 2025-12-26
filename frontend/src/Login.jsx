import React, { useState } from "react";
import axios from "axios";

function Login({ setToken, onSwitch }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const login = async () => {
    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/auth/login",
        {
        email, 
        password 
        }
      );

      localStorage.setItem("token", res.data.access_token);
      setToken(res.data.access_token);
    } catch {
      setError("Invalid credentials");
    }
  };

  return (
    <div className="auth-box">
      <h2>Login</h2>

      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />

      <button onClick={login}>Login</button>

      {error && <p className="error">{error}</p>}

      <p className="link" onClick={onSwitch}>
        Create an account
      </p>
    </div>
  );
}

export default Login;
