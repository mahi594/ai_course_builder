export default function Lesson({ lesson }) {
  return (
    <div className="ml-4 mt-4">
      <h3 className="font-semibold">{lesson.lesson_title}</h3>

      <ul className="list-disc ml-6 text-sm">
        {lesson.notes.map((n, i) => (
          <li key={i}>{n}</li>
        ))}
      </ul>

      <div className="mt-2">
        <p className="font-medium">Quiz:</p>
        {lesson.quiz.map((q, i) => (
          <p key={i} className="text-sm">
            ❓ {q.question}
          </p>
        ))}
      </div>
    </div>
  );
}
