export default function ModuleCard({ module }) {
  const videoId = module.source.split("v=")[1];

  return (
    <div className="border rounded-xl p-4 space-y-4">
      <h2 className="text-2xl font-semibold">{module.course_title}</h2>

      {/* Video */}
      <iframe
        className="w-full h-64 rounded"
        src={`https://www.youtube.com/embed/${videoId}`}
        allowFullScreen
      />

      {/* Lessons */}
      {module.lessons.map((lesson) => (
        <LessonCard
          key={lesson.lesson_number}
          lesson={lesson}
        />
      ))}
    </div>
  );
}
