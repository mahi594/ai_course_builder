from backend.services.course_builder_free import build_course_from_topic
from backend.utils.job_store import set_job_result, set_job_error

def run_course_job(job_id, topic, difficulty, videos_per_topic):
    try:
        course = build_course_from_topic(
            topic=topic,
            difficulty=difficulty,
            videos_per_topic=videos_per_topic
        )
        set_job_result(job_id, course)
    except Exception as e:
        set_job_error(job_id, e)
