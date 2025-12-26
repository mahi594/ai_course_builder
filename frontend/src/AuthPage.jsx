import React, { useState } from "react";
import Login from "./Login";
import Signup from "./Signup";

function AuthPage({ setToken }) {
  const [mode, setMode] = useState("login");

  return (
    <>
      {mode === "login" ? (
        <Login
          setToken={setToken}
          onSwitch={() => setMode("signup")}
        />
      ) : (
        <Signup
          onSwitch={() => setMode("login")}
        />
      )}
    </>
  );
}

export default AuthPage;
