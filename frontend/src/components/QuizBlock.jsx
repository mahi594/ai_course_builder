export default function QuizBlock({ quiz }) {
  if (!quiz || quiz.length === 0) return null;

  return (
    <div>
      <h4 className="font-semibold mt-4 mb-2">Quiz</h4>

      {quiz.map((q, idx) => (
        <div key={idx} className="mb-3">
          <p className="font-medium">{q.question}</p>
          <ul className="pl-4">
            {q.options.map((opt, i) => (
              <li key={i}>• {opt}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}
