import React, { useState, useEffect } from "react";
import axios from "axios";
import Login from "./Login";
import "./App.css";

function App() {
  /* =====================
     AUTH
  ====================== */
  const [token, setToken] = useState(localStorage.getItem("token"));

  /* =====================
     COURSE STATE
  ====================== */
  const [topic, setTopic] = useState("");
  const [difficulty, setDifficulty] = useState("Beginner");
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(false);

  /* =====================
     PROGRESS TRACKING
  ====================== */
  const [completed, setCompleted] = useState(
    JSON.parse(localStorage.getItem("completedModules")) || {}
  );

  useEffect(() => {
    localStorage.setItem("completedModules", JSON.stringify(completed));
  }, [completed]);

  /* =====================
     AUTH GATE
  ====================== */
  if (!token) {
    return <Login setToken={setToken} />;
  }

  /* =====================
     LOGOUT
  ====================== */
  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("completedModules");
    setToken(null);
  };

  /* =====================
     GENERATE COURSE
  ====================== */
  const generateCourse = async () => {
    if (!topic.trim()) {
      alert("Please enter a topic");
      return;
    }

    setLoading(true);
    setCourse(null);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/generate-course", // change to Render URL after deploy
        { topic, difficulty },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setCourse(res.data);
      setCompleted({});
    } catch (err) {
      alert("Failed to generate course");
    }

    setLoading(false);
  };

  /* =====================
     PROGRESS
  ====================== */
  const progress =
    course?.modules?.length
      ? Math.round(
          (Object.values(completed).filter(Boolean).length /
            course.modules.length) *
            100
        )
      : 0;

  const toggleComplete = (index) => {
    setCompleted({ ...completed, [index]: !completed[index] });
  };

  /* =====================
     UI
  ====================== */
  return (
    <div className="container">
      {/* HEADER */}
      <div className="header">
        <h1>AI Course Builder</h1>
        <button className="logout-btn" onClick={logout}>
          Logout
        </button>
      </div>

      {/* INPUTS */}
      <div className="controls">
        <input
          className="input"
          placeholder="Enter a topic (e.g. Machine Learning)"
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
      </div>

      {loading && <p className="loading">⏳ Generating course…</p>}

      {/* COURSE */}
      {course && (
        <>
          <h2 className="course-title">{course.course_title}</h2>

          {/* PROGRESS BAR */}
          <div className="progress-wrapper">
            <strong>Progress: {progress}%</strong>
            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{ width: `${progress}%` }}
              />
            </div>
          </div>

          {/* MODULES */}
          {course.modules?.length > 0 ? (
            course.modules.map((m, i) => {
              const videoId =
                m.video_url && m.video_url.includes("v=")
                  ? m.video_url.split("v=")[1].split("&")[0]
                  : null;

              return (
                <div className="card" key={i}>
                  <div className="card-header">
                    <h3>{m.module_title}</h3>

                    <label className="checkbox">
                      <input
                        type="checkbox"
                        checked={completed[i] || false}
                        onChange={() => toggleComplete(i)}
                      />
                      Completed
                    </label>
                  </div>

                  {/* YOUTUBE EMBED */}
                  {videoId && (
                    <iframe
                      width="100%"
                      height="315"
                      src={`https://www.youtube.com/embed/${videoId}`}
                      title={m.module_title}
                      allowFullScreen
                    />
                  )}

                  {/* NOTES */}
                  <h4>Notes</h4>
                  <ul>
                    {Array.isArray(m.notes) &&
                      m.notes.map((n, j) => <li key={j}>{n}</li>)}
                  </ul>

                  {/* QUIZ */}
                  <h4>Quiz</h4>
                  <ul>
                    {Array.isArray(m.quiz) &&
                      m.quiz.map((q, j) => (
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
              );
            })
          ) : (
            <p>No modules generated.</p>
          )}

          {/* RECOMMENDATIONS */}
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
