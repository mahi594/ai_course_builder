import { useState } from "react";

export default function CourseForm({ onGenerate }) {
  const [topic, setTopic] = useState("");
  const [difficulty, setDifficulty] = useState("beginner");

  return (
    <div className="space-y-4">
      <input
        className="w-full p-2 border rounded"
        placeholder="Enter topic (e.g. Deep Learning)"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <select
        className="w-full p-2 border rounded"
        value={difficulty}
        onChange={(e) => setDifficulty(e.target.value)}
      >
        <option value="beginner">Beginner</option>
        <option value="intermediate">Intermediate</option>
        <option value="advanced">Advanced</option>
      </select>

      <button
        onClick={() => onGenerate({ topic, difficulty })}
        className="w-full bg-black text-white py-2 rounded"
      >
        Generate Course
      </button>
    </div>
  );
}
