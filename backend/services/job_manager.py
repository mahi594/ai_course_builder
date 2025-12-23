import uuid
import json
import os
from datetime import datetime

JOB_DIR = "backend/data/jobs"
os.makedirs(JOB_DIR, exist_ok=True)


def create_job():
    job_id = str(uuid.uuid4())
    job_path = f"{JOB_DIR}/{job_id}.json"

    with open(job_path, "w") as f:
        json.dump({
            "job_id": job_id,
            "status": "queued",
            "created_at": datetime.utcnow().isoformat(),
            "result": None,
            "error": None
        }, f)

    return job_id


def update_job(job_id, **updates):
    job_path = f"{JOB_DIR}/{job_id}.json"
    with open(job_path, "r") as f:
        data = json.load(f)

    data.update(updates)

    with open(job_path, "w") as f:
        json.dump(data, f, indent=2)


def get_job(job_id):
    job_path = f"{JOB_DIR}/{job_id}.json"
    if not os.path.exists(job_path):
        return None

    with open(job_path, "r") as f:
        return json.load(f)
