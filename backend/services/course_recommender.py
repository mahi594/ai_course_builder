def get_course_recommendations(topic: str):
    topic_lower = topic.lower()

    recommendations = {
        "coursera": [
            {
                "title": f"{topic.title()} Specialization",
                "url": f"https://www.coursera.org/search?query={topic_lower}"
            }
        ],
        "udemy": [
            {
                "title": f"Complete {topic.title()} Bootcamp",
                "url": f"https://www.udemy.com/courses/search/?q={topic_lower}"
            }
        ],
        "free": [
            {
                "title": f"{topic.title()} – FreeCodeCamp",
                "url": f"https://www.youtube.com/results?search_query={topic_lower}+full+course"
            }
        ]
    }

    return recommendations
