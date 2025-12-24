import React, { useState } from "react";
import axios from "axios";

function Signup({ setShowSignup }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const signup = async () => {
    try {
      await axios.post("http://127.0.0.1:8000/auth/signup", {
        email,
        password,
      });
      alert("Account created. Please login.");
      setShowSignup(false);
    } catch {
      alert("Signup failed");
    }
  };

  return (
    <div className="auth-card">
      <h2>Sign Up</h2>

      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      />

      <button onClick={signup}>Create Account</button>

      <p>
        Already have an account?{" "}
        <span onClick={() => setShowSignup(false)}>Login</span>
      </p>
    </div>
  );
}

export default Signup;
