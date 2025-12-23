def get_course_syllabus(topic: str, difficulty="beginner"):
    topic = topic.lower().strip()

    SYLLABUS = {
        "machine learning": [
            "introduction to machine learning",
            "types of machine learning",
            "supervised learning",
            "unsupervised learning",
            "regression algorithms",
            "classification algorithms",
            "model evaluation"
        ],
        "deep learning": [
            "introduction to deep learning",
            "neural networks basics",
            "activation functions",
            "loss functions",
            "backpropagation",
            "cnn basics",
            "rnn and lstm",
            "transformers overview"
        ],
        "web development": [
            "html basics",
            "css fundamentals",
            "javascript basics",
            "react fundamentals",
            "backend fundamentals",
            "deployment basics"
        ]
    }

    if topic in SYLLABUS:
        return SYLLABUS[topic]

    # 🔥 GUARANTEED FALLBACK (never empty)
    return [
        f"{topic} basics",
        f"{topic} fundamentals",
        f"{topic} intermediate concepts",
        f"{topic} advanced concepts",
        f"{topic} real world applications"
    ]
