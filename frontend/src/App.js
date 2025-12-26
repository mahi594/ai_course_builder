import React, { useState } from "react";
import axios from "axios";
import Login from "./Login";
import Signup from "./Signup";
import "./App.css";

// ✅ API URL (local OR deployed)
const API_URL =
  process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";

// ✅ Robust YouTube embed helper
const getYouTubeEmbedUrl = (url) => {
  if (!url) return null;

  if (url.includes("youtube.com/watch")) {
    const videoId = new URL(url).searchParams.get("v");
    return `https://www.youtube.com/embed/${videoId}`;
  }

  if (url.includes("youtu.be")) {
    const videoId = url.split("youtu.be/")[1];
    return `https://www.youtube.com/embed/${videoId}`;
  }

  if (url.includes("youtube.com/embed")) {
    return url;
  }

  return null;
};

function App() {
  // 🔐 Auth state
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [showSignup, setShowSignup] = useState(false);

  // 📘 Course state
  const [topic, setTopic] = useState("");
  const [difficulty, setDifficulty] = useState("Beginner");
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(false);

  // 🚪 Logout
  const logout = () => {
    localStorage.removeItem("token");
    setToken(null);
    setCourse(null);
  };

  // 🧠 Generate course
  const generateCourse = async () => {
    if (!topic) {
      alert("Please enter a topic");
      return;
    }

    setLoading(true);
    setCourse(null);

    try {
      const res = await axios.post(
        `${API_URL}/generate-course`,
        { topic, difficulty },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setCourse(res.data);
    } catch (err) {
      alert("Failed to generate course");
    }

    setLoading(false);
  };

  // 🔐 Auth Gate
  if (!token) {
    return showSignup ? (
      <Signup onSwitch={() => setShowSignup(false)} />
    ) : (
      <Login
        setToken={setToken}
        onSwitch={() => setShowSignup(true)}
      />
    );
  }

  // 🎓 Main App
  return (
    <div className="container">
      <header className="top-bar">
        <h1>🎓 AI Course Builder</h1>
        <button className="logout-btn" onClick={logout}>
          Logout
        </button>
      </header>

      <div className="controls">
        <input
          placeholder="Enter a topic (e.g. Machine Learning)"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
        />

        <select
          value={difficulty}
          onChange={(e) => setDifficulty(e.target.value)}
        >
          <option>Beginner</option>
          <option>Intermediate</option>
          <option>Advanced</option>
        </select>

        <button onClick={generateCourse}>
          Generate Course
        </button>
      </div>

      {loading && <p className="loading">⏳ Generating course...</p>}

      {course && (
        <>
          <h2 className="course-title">{course.course_title}</h2>

          {course.modules.map((m, i) => (
            <div className="card" key={i}>
              <h3>{m.module_title}</h3>

              {/* ✅ YouTube Embed */}
              {m.video_url && (
                <iframe
                  width="100%"
                  height="315"
                  src={getYouTubeEmbedUrl(m.video_url)}
                  title={m.module_title}
                  frameBorder="0"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowFullScreen
                />
              )}

              <h4>📘 Notes</h4>
              <ul>
                {m.notes.map((n, j) => (
                  <li key={j}>{n}</li>
                ))}
              </ul>

              <h4>📝 Quiz</h4>
              <ul>
                {m.quiz.map((q, j) => (
                  <li key={j}>
                    <strong>{q.question}</strong>
                    {q.options && (
                      <ul>
                        {q.options.map((op, k) => (
                          <li key={k}>{op}</li>
                        ))}
                      </ul>
                    )}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </>
      )}
    </div>
  );
}

export default App;
