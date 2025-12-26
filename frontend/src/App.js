import React, { useState } from "react";
import axios from "axios";
import Login from "./Login";
import Signup from "./Signup";
import "./App.css";

// ✅ API URL (local + deployed)
const API_URL =
  process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";

// ✅ Robust YouTube ID extractor
const getYouTubeId = (url) => {
  if (!url) return null;

  const vMatch = url.match(/v=([^&]+)/);
  if (vMatch) return vMatch[1];

  const shortMatch = url.match(/youtu\.be\/([^?]+)/);
  if (shortMatch) return shortMatch[1];

  return null;
};

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [showSignup, setShowSignup] = useState(false);

  const [topic, setTopic] = useState("");
  const [difficulty, setDifficulty] = useState("Beginner");
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(false);

  // 🔐 AUTH GATE
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

  // 🚪 Logout
  const logout = () => {
    localStorage.removeItem("token");
    setToken(null);
    setCourse(null);
  };

  // 🎓 Generate Course
  const generateCourse = async () => {
    if (!topic.trim()) {
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

  return (
    <div className="container">
      {/* Header */}
      <div className="top-bar">
        <h1>🎓 AI Course Builder</h1>
        <button className="logout-btn" onClick={logout}>
          Logout
        </button>
      </div>

      {/* Inputs */}
      <input
        className="input"
        placeholder="Enter topic (e.g. Machine Learning)"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <select
        className="select"
        value={difficulty}
        onChange={(e) => setDifficulty(e.target.value)}
      >
        <option>Beginner</option>
        <option>Intermediate</option>
        <option>Advanced</option>
      </select>

      <button className="primary-btn" onClick={generateCourse}>
        Generate Course
      </button>

      {loading && <p className="loading">⏳ Generating course…</p>}

      {/* Course Output */}
      {course && (
        <>
          <h2 className="course-title">{course.course_title}</h2>

          {course.modules.map((m, i) => {
            const videoId = getYouTubeId(m.video_url);

            return (
              <div className="card" key={i}>
                <h3>{m.module_title}</h3>

                {/* 🎥 YouTube Embed */}
                {videoId && (
                  <iframe
                    width="100%"
                    height="315"
                    src={`https://www.youtube.com/embed/${videoId}`}
                    title={m.module_title}
                    frameBorder="0"
                    allowFullScreen
                  />
                )}

                {/* Notes */}
                <h4>📘 Notes</h4>
                <ul>
                  {m.notes.map((n, j) => (
                    <li key={j}>{n}</li>
                  ))}
                </ul>

                {/* Quiz */}
                <h4>📝 Quiz</h4>
                <ul>
                  {m.quiz.map((q, j) => (
                    <li key={j}>
                      <strong>{q.question}</strong>
                    </li>
                  ))}
                </ul>
              </div>
            );
          })}
        </>
      )}
    </div>
  );
}

export default App;

console.log("API URL:", API_URL);
