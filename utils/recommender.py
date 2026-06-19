import re
from utils.domain import (
    detect_domain,
    get_domain_info,
    get_domain_keywords,
    get_domain_jobs,
    get_job_skills,
    detect_seniority,
)


def recommend_jobs(resume_text):
    domain_key = detect_domain(resume_text)
    domain_info = get_domain_info(domain_key)
    domain_jobs = get_domain_jobs(domain_key)
    domain_label = domain_info["label"]

    resume_text_lower = resume_text.lower()
    seniority = detect_seniority(resume_text_lower)

    recommendations = []
    for job_title in domain_jobs:
        job_skills = get_job_skills(domain_key, job_title)
        matched_count = count_matched_skills(resume_text_lower, job_skills)
        total = len(job_skills)
        score = round((matched_count / total) * 100) if total > 0 else 0
        score = max(5, min(100, score))

        title = f"{seniority} {job_title}" if seniority else job_title
        recommendations.append({
            "title": title,
            "confidence": score,
        })

    recommendations.sort(key=lambda x: -x["confidence"])
    return recommendations[:10]


def count_matched_skills(text_lower, skills):
    count = 0
    for skill in skills:
        pattern = r'(?<!\w)' + re.escape(skill) + r'(?!\w)'
        if re.search(pattern, text_lower):
            count += 1
    return count
