import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [topic, setTopic] = useState("");
  const [difficulty, setDifficulty] = useState("Beginner");
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateCourse = async () => {
    setLoading(true);
    setCourse(null);

    try {
      const res = await axios.post("http://127.0.0.1:8000/generate-course", {
        topic,
        difficulty,
      });
      setCourse(res.data);
    } catch (err) {
      alert("Failed to generate course");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>AI Course Builder</h1>

      <input
        placeholder="Enter topic"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <select value={difficulty} onChange={(e) => setDifficulty(e.target.value)}>
        <option>Beginner</option>
        <option>Intermediate</option>
        <option>Advanced</option>
      </select>

      <button onClick={generateCourse}>Generate Course</button>

      {loading && <p>⏳ Generating course…</p>}

      {course && (
        <>
          <h2>{course.course_title}</h2>
          <p>📘 Course generated using syllabus-based learning.</p>

          {Array.isArray(course.modules) && course.modules.length > 0 ? (
            course.modules.map((module, idx) => (
              <div className="card" key={idx}>
                <h3>{module.module_title}</h3>

                {/* YouTube Embed */}
                {module.video_url && (
                  <iframe
                    width="100%"
                    height="315"
                    src={`https://www.youtube.com/embed/${module.video_url.split("v=")[1]}`}
                    title={module.module_title}
                    frameBorder="0"
                    allowFullScreen
                  />
                )}

                <h4>Notes</h4>
                <ul>
                  {module.notes.map((n, i) => (
                    <li key={i}>{n}</li>
                  ))}
                </ul>

                <h4>Quiz</h4>
                <ul>
                  {module.quiz.map((q, i) => (
                    <li key={i}>
                      <strong>{q.question}</strong>
                      {q.options && (
                        <ul>
                          {q.options.map((op, j) => (
                            <li key={j}>{op}</li>
                          ))}
                        </ul>
                      )}
                    </li>
                  ))}
                </ul>
              </div>
            ))
          ) : (
            <p>No modules generated.</p>
          )}

          {/* Recommendations */}
          {course.recommendations && (
            <>
              <h3>🎓 Recommended Courses</h3>
              <ul>
                {course.recommendations?.udemy?.map((item, i) => (
  <p key={i}>
    <a href={item.url} target="_blank" rel="noreferrer">
      {item.title}
    </a>
  </p>
))}

                {course.recommendations?.coursera?.map((item, i) => (
  <p key={i}>
    <a href={item.url} target="_blank" rel="noreferrer">
      {item.title}
    </a>
  </p>
))}

              </ul>
            </>
          )}
        </>
      )}
    </div>
  );
}

export default App;
