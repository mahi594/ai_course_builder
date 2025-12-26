import React, { useState } from "react";
import axios from "axios";

function Signup({ onSwitch }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState("");

  const signup = async () => {
    try {
      await axios.post(
        "http://127.0.0.1:8000/auth/signup",
        null,
         { email, 
           password } 
      );
      setMsg("Signup successful. Please login.");
    } catch {
      setMsg("Signup failed");
    }
  };

  return (
    <div className="auth-box">
      <h2>Signup</h2>

      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />

      <button onClick={signup}>Signup</button>

      {msg && <p>{msg}</p>}

      <p className="link" onClick={onSwitch}>
        Back to login
      </p>
    </div>
  );
}

export default Signup;
