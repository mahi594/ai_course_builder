import Module from "./Module";

export default function CourseViewer({ course }) {
  return (
    <div className="mt-6 space-y-6">
      <h1 className="text-2xl font-bold">{course.course_title}</h1>

      {course.modules.map((module, idx) => (
        <Module key={idx} module={module} />
      ))}
    </div>
  );
}
