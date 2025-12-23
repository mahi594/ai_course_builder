from backend.services.course_builder_free import build_course_from_topic
from backend.services.job_manager import update_job


def run_course_job(job_id, topic, difficulty, videos_per_topic):
    try:
        update_job(job_id, status="processing")

        course = build_course_from_topic(
            topic=topic,
            difficulty=difficulty,
            videos_per_topic=videos_per_topic
        )

        update_job(
            job_id,
            status="completed",
            result=course
        )

    except Exception as e:
        update_job(
            job_id,
            status="failed",
            error=str(e)
        )
