import re
import textstat


ACTION_VERBS = {
    "developed", "designed", "implemented", "led", "managed", "created",
    "built", "optimized", "improved", "delivered", "achieved", "launched",
    "architected", "engineered", "deployed", "orchestrated", "spearheaded",
    "established", "transformed", "automated", "integrated", "configured",
    "mentored", "coordinated", "drove", "generated", "produced",
}

TONE_INDICATORS = {
    "professional": ["collaborated", "strategic", "results-driven", "cross-functional"],
    "analytical": ["analyzed", "evaluated", "quantified", "measured"],
    "leadership": ["supervised", "directed", "mentored", "coached"],
}


def evaluate_communication(text):
    if not text or len(text.strip()) < 20:
        return {
            "clarity": 50,
            "vocabulary": 50,
            "professionalism": 50,
            "grammar": 50,
            "overall": 50,
            "details": "Insufficient text for evaluation.",
        }

    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 5]
    total_sentences = len(sentences) or 1

    words = re.findall(r'\b[a-zA-Z]+\b', text)
    total_words = len(words) or 1
    unique_words = len(set(w.lower() for w in words))
    avg_sentence_length = total_words / total_sentences

    action_verb_count = sum(1 for w in words if w.lower() in ACTION_VERBS)
    action_verb_density = action_verb_count / total_sentences

    flesch = textstat.flesch_reading_ease(text)
    flesch = max(0, min(100, flesch))

    grade_level = textstat.flesch_kincaid_grade(text)

    clarity = min(100, flesch * 0.6 + (100 - grade_level * 5) * 0.4)
    clarity = max(20, clarity)

    vocab_ratio = unique_words / total_words
    vocabulary = min(100, vocab_ratio * 100 + action_verb_density * 15)
    vocabulary = max(20, min(100, vocabulary))

    prof_count = sum(
        1 for phrase_list in TONE_INDICATORS.values()
        for phrase in phrase_list
        if phrase.lower() in text.lower()
    )
    professionalism = min(100, 50 + action_verb_density * 20 + prof_count * 5)
    professionalism = max(20, min(100, professionalism))

    grammar_issues = _detect_grammar_issues(text)
    grammar_penalty = min(40, grammar_issues * 5)
    grammar = max(20, 100 - grammar_penalty)

    overall = (clarity * 0.25 + vocabulary * 0.25 + professionalism * 0.30 + grammar * 0.20)

    details = []
    if action_verb_density < 1.0:
        details.append("Consider adding more action verbs (e.g., developed, led, implemented).")
    if avg_sentence_length > 25:
        details.append("Some sentences are very long. Try breaking them into shorter, clearer statements.")
    elif avg_sentence_length < 8:
        details.append("Sentences are very short. Vary sentence structure for better readability.")
    if grade_level > 16:
        details.append("Writing is very complex. Consider simplifying technical explanations where possible.")
    if grammar_issues > 0:
        details.append(f"Potential grammar issues detected: {grammar_issues}.")

    return {
        "clarity": round(clarity),
        "vocabulary": round(vocabulary),
        "professionalism": round(professionalism),
        "grammar": round(grammar),
        "overall": round(overall),
        "details": " ".join(details) if details else "Communication quality is strong.",
    }


def _detect_grammar_issues(text):
    issues = 0

    subject_verb = re.findall(r'\b(He|She|It)\s+(are|were|have)\b', text, re.IGNORECASE)
    issues += len(subject_verb)

    double_space = re.findall(r'\w\s{2,}\w', text)
    issues += len(double_space)

    run_ons = re.findall(r'[a-z]+,[a-z]+', text)
    issues += len(run_ons)

    return issues
