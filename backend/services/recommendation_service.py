def recommend_courses(topic: str):
    return {
        "udemy": [
            {
                "title": f"{topic.title()} Masterclass",
                "url": "https://www.udemy.com/"
            }
        ],
        "coursera": [
            {
                "title": f"{topic.title()} Specialization",
                "url": "https://www.coursera.org/"
            }
        ]
    }
