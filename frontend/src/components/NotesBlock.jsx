export default function NotesBlock({ notes }) {
  return (
    <div>
      <h4 className="font-semibold mb-2">Notes</h4>
      <ul className="list-disc pl-6 space-y-1">
        {notes.map((note, idx) => (
          <li key={idx}>{note}</li>
        ))}
      </ul>
    </div>
  );
}
