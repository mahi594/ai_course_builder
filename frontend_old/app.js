let jobId = null;

async function generateCourse() {
  const topic = document.getElementById("topic").value;
  const difficulty = document.getElementById("difficulty").value;

  document.getElementById("status").innerText = "⏳ Generating course...";

  const res = await fetch("http://127.0.0.1:8000/generate-course", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      topic,
      difficulty,
      videos_per_topic: 1
    })
  });

  const data = await res.json();
  jobId = data.job_id;

  pollStatus();
}

async function pollStatus() {
  const res = await fetch(`http://127.0.0.1:8000/status/${jobId}`);
  const data = await res.json();

  if (data.status === "processing") {
    setTimeout(pollStatus, 3000);
  } else if (data.status === "completed") {
    document.getElementById("status").innerText = "✅ Course Ready!";
    renderCourse(data.result);
  } else {
    document.getElementById("status").innerText = "❌ Error: " + data.error;
  }
}

function renderCourse(course) {
  let html = `<h2>${course.course_title}</h2>`;

  course.modules.forEach(m => {
    html += `<h3>${m.course_title}</h3>`;

    m.lessons.forEach(l => {
      html += `<h4>${l.lesson_title}</h4><ul>`;
      l.notes.forEach(n => html += `<li>${n}</li>`);
      html += "</ul>";
    });
  });

  document.getElementById("output").innerHTML = html;
}
