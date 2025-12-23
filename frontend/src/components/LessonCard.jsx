export default function LessonCard({ lesson }) {
  return (
    <div className="bg-gray-50 p-4 rounded-lg space-y-3">
      <h3 className="text-xl font-medium">
        {lesson.lesson_number}. {lesson.lesson_title}
      </h3>

      <NotesBlock notes={lesson.notes} />
      <QuizBlock quiz={lesson.quiz} />
    </div>
  );
}
