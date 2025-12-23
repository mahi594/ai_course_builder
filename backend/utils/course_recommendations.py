def recommend_courses(topic: str):
    topic = topic.lower()

    return {
        "udemy": f"https://www.udemy.com/courses/search/?q={topic}",
        "coursera": f"https://www.coursera.org/search?query={topic}",
        "youtube": f"https://www.youtube.com/results?search_query={topic}+full+course"
    }
