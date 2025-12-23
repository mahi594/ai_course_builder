export default function CourseView({ course }) {
  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">{course.course_title}</h1>
      <p className="text-gray-600 capitalize">{course.difficulty}</p>

      {course.modules.map((module, idx) => (
        <ModuleCard key={idx} module={module} />
      ))}
    </div>
  );
}
