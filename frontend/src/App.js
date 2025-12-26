import React, { useState, useEffect } from "react";
import axios from "axios";
import Login from "./Login";
import "./App.css";
import AuthPage from "./AuthPage";

const API_URL = "https://ai-course-builder-1-smgs.onrender.com"; 
// ⬆️ change to localhost if testing locally

function App() {
  /* =========================
     AUTH
  ========================= */
  const [token, setToken] = useState(localStorage.getItem("token"));

  /* =========================
     COURSE STATES
  ========================= */
  const [topic, setTopic] = useState("");
  const [difficulty, setDifficulty] = useState("Beginner");
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(false);

  /* =========================
     PROGRESS TRACKING
  ========================= */
  const [completed, setCompleted] = useState(
    JSON.parse(localStorage.getItem("completedModules")) || {}
  );

  useEffect(() => {
    localStorage.setItem("completedModules", JSON.stringify(completed));
  }, [completed]);

  /* =========================
     AUTH GATE
  ========================= */


  if (!token) {
   return <AuthPage setToken={setToken} />;
}


  /* =========================
     HANDLERS
  ========================= */
  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("completedModules");
    setToken(null);
  };

  const toggleComplete = (index) => {
    setCompleted((prev) => ({
      ...prev,
      [index]: !prev[index],
    }));
  };

  const progress =
    course?.modules?.length
      ? Math.round(
          (Object.values(completed).filter(Boolean).length /
            course.modules.length) *
            100
        )
      : 0;

  const generateCourse = async () => {
    if (!topic) {
      alert("Please enter a topic");
      return;
    }

    setLoading(true);
    setCourse(null);
    setCompleted({});

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

  /* =========================
     UI
  ========================= */
  return (
    <div className="container">
      <button
        onClick={logout}
        style={{
          background: "#d32f2f",
          color: "#fff",
          padding: "8px 14px",
          border: "none",
          borderRadius: "6px",
          float: "right",
          cursor: "pointer",
        }}
      >
        Logout
      </button>

      <h1>AI Course Builder</h1>

      <input
        placeholder="Enter course topic (e.g. Machine Learning)"
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

      <button onClick={generateCourse}>Generate Course</button>

      {loading && <p>⏳ Generating course…</p>}

      {/* =========================
          COURSE OUTPUT
      ========================= */}
      {course && (
        <>
          <h2>{course.course_title}</h2>
          <p>📘 Course generated using syllabus-based learning.</p>

          {/* Progress Bar */}
          {course.modules?.length > 0 && (
            <div style={{ margin: "20px 0" }}>
              <strong>Progress: {progress}%</strong>
              <div style={{ background: "#ddd", height: 10, borderRadius: 5 }}>
                <div
                  style={{
                    width: `${progress}%`,
                    background: "#4caf50",
                    height: "100%",
                    borderRadius: 5,
                  }}
                />
              </div>
            </div>
          )}

          {/* Modules */}
          {course.modules?.map((m, i) => (
            <div className="card" key={i}>
              <h3>{m.module_title}</h3>

              {/* Completion */}
              <label style={{ display: "block", marginBottom: 10 }}>
                <input
                  type="checkbox"
                  checked={completed[i] || false}
                  onChange={() => toggleComplete(i)}
                />{" "}
                Mark as completed
              </label>

              {/* YouTube Embed */}
              {m.video_url && m.video_url.includes("v=") && (
                <iframe
                  width="100%"
                  height="315"
                  src={`https://www.youtube.com/embed/${
                    m.video_url.split("v=")[1]
                  }`}
                  title={m.module_title}
                  allowFullScreen
                />
              )}

              {/* Notes */}
              <h4>Notes</h4>
              <ul>
                {m.notes.map((n, j) => (
                  <li key={j}>{n}</li>
                ))}
              </ul>

              {/* Quiz */}
              <h4>Quiz</h4>
              <ul className="quiz">
                {m.quiz.map((q, j) => (
                  <li key={j} className="quiz-item">
                    <strong>{q.question}</strong>
                    {q.options && (
                      <ul className="quiz-options">
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

          {/* Recommendations */}
          {course.recommendations && (
            <>
              <h3>🎓 Recommended Courses</h3>

              {course.recommendations.udemy?.map((c, i) => (
                <p key={i}>
                  <a href={c.url} target="_blank" rel="noreferrer">
                    {c.title}
                  </a>
                </p>
              ))}

              {course.recommendations.coursera?.map((c, i) => (
                <p key={i}>
                  <a href={c.url} target="_blank" rel="noreferrer">
                    {c.title}
                  </a>
                </p>
              ))}
            </>
          )}
        </>
      )}
    </div>
  );
}

export default App;
