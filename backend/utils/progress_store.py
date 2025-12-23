progress = {}

def init_course(course_id):
    progress[course_id] = {}

def mark_lesson_done(course_id, module, lesson):
    progress.setdefault(course_id, {})
    progress[course_id][f"{module}-{lesson}"] = True

def get_progress(course_id):
    return progress.get(course_id, {})
