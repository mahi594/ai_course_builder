import Lesson from "./Lesson";

export default function Module({ module }) {
  return (
    <div className="border rounded p-4">
      <h2 className="text-xl font-semibold">{module.course_title}</h2>

      {module.lessons.map((lesson) => (
        <Lesson key={lesson.lesson_number} lesson={lesson} />
      ))}
    </div>
  );
}
