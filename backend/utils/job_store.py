import uuid
import json
import os
from threading import Lock

# --------------------------------------------------
# Persistent Job Store (JSON based)
# --------------------------------------------------

JOB_FILE = "jobs.json"
LOCK = Lock()


def _load_jobs():
    if not os.path.exists(JOB_FILE):
        return {}
    with open(JOB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_jobs(jobs):
    with open(JOB_FILE, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2)


def create_job():
    with LOCK:
        jobs = _load_jobs()
        job_id = str(uuid.uuid4())
        jobs[job_id] = {
            "status": "processing",
            "result": None,
            "error": None
        }
        _save_jobs(jobs)
        return job_id


def set_job_result(job_id, result):
    with LOCK:
        jobs = _load_jobs()
        if job_id in jobs:
            jobs[job_id]["status"] = "completed"
            jobs[job_id]["result"] = result
            _save_jobs(jobs)


def set_job_error(job_id, error):
    with LOCK:
        jobs = _load_jobs()
        if job_id in jobs:
            jobs[job_id]["status"] = "failed"
            jobs[job_id]["error"] = str(error)
            _save_jobs(jobs)


def get_job(job_id):
    jobs = _load_jobs()
    return jobs.get(job_id)
