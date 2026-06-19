import re
from utils.domain import (
    detect_domain,
    get_domain_info,
    get_domain_keywords,
    extract_domain_skills,
    get_all_skills,
)

SCOPE_INDICATORS = [
    "production", "production-grade", "enterprise", "enterprise-level",
    "global", "worldwide", "international", "multi-country",
    "large-scale", "high-volume", "high-traffic",
    "millions of", "billions of", "thousands of users",
    "cross-border", "multi-region", "distributed",
    "at scale", "multi-million", "multi-billion",
    "fortune 500", "enterprise-wide", "organization-wide",
]

SOFT_SKILL_INDICATORS = [
    "cross-functional", "stakeholder management", "vendor management",
    "team leadership", "mentoring", "collaboration",
    "client-facing", "client management", "customer presentation",
    "strategic planning", "roadmap", "decision making",
    "project management", "scrum master", "negotiation",
    "conflict resolution", "executive communication",
    "change management", "agile transformation",
    "c-level presentation", "board reporting",
]


def count_quantified_achievements(text):
    patterns = [
        r'\b\d+\s*%[^\w]?', r'\bincreased\b', r'\bdecreased\b',
        r'\breduced\b', r'\bimproved\b', r'\bgrew\b',
        r'\b\d+x\b', r'\b\d+\s*(?:million|billion|thousand)\b',
        r'\$\s*\d+(?:\.\d+)?[kKmMbB]?\b', r'\b\d+\s*(?:users|customers|clients)\b',
        r'\b\d+\s*(?:revenue|sales|profit)\b',
    ]
    count = 0
    for pat in patterns:
        count += len(re.findall(pat, text, re.IGNORECASE))
    return count


def estimate_project_depth(text):
    lines = text.split("\n")
    project_sections = []
    current = []
    keywords = {"project", "experience", "role", "work", "achievement"}
    in_section = False
    for line in lines:
        stripped = line.strip().lower()
        if any(k in stripped for k in keywords) and len(stripped) < 50:
            if current:
                project_sections.append(" ".join(current))
            current = [line]
            in_section = True
        elif in_section and stripped:
            current.append(line)
        else:
            in_section = False
    if current:
        project_sections.append(" ".join(current))

    depth = 0
    for section in project_sections:
        words = len(section.split())
        if words > 50:
            depth += 2
        elif words > 20:
            depth += 1
        if any(kw in section.lower() for kw in ["built", "developed", "designed", "led", "created"]):
            depth += 1
    return min(100, depth * 10)


def analyze_hard_skill_gaps(resume_text, jd_text, domain):
    jd_skills = extract_domain_skills(jd_text, domain)
    resume_skills = extract_domain_skills(resume_text, domain)
    return sorted(jd_skills - resume_skills)


def analyze_scope_gaps(resume_text, jd_text):
    text_lower_r = resume_text.lower()
    text_lower_j = jd_text.lower()
    gaps = []
    for indicator in SCOPE_INDICATORS:
        pattern = r'(?<!\w)' + re.escape(indicator) + r'(?!\w)'
        in_jd = re.search(pattern, text_lower_j)
        in_resume = re.search(pattern, text_lower_r)
        if in_jd and not in_resume:
            gaps.append(indicator)
    return gaps


def analyze_soft_skill_gaps(resume_text, jd_text):
    text_lower_r = resume_text.lower()
    text_lower_j = jd_text.lower()
    gaps = []
    for indicator in SOFT_SKILL_INDICATORS:
        pattern = r'(?<!\w)' + re.escape(indicator) + r'(?!\w)'
        in_jd = re.search(pattern, text_lower_j)
        in_resume = re.search(pattern, text_lower_r)
        if in_jd and not in_resume:
            gaps.append(indicator)
    return gaps


def calculate_score(resume_text, job_desc=None, comm_score=None):
    comm = comm_score or {"overall": 60}
    domain = detect_domain(resume_text)

    if job_desc:
        return _path_with_jd(resume_text, job_desc, comm, domain)
    else:
        return _path_without_jd(resume_text, comm, domain)


def _path_with_jd(resume_text, job_desc, comm, domain):
    resume_skills = extract_domain_skills(resume_text, domain)
    jd_skills = extract_domain_skills(job_desc, domain)

    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills
    total_jd = len(jd_skills)

    keyword_match_score = round((len(matched) / total_jd * 100)) if total_jd > 0 else 0

    hard_skill_gaps = sorted(jd_skills - resume_skills)
    scope_gaps = analyze_scope_gaps(resume_text, job_desc)
    soft_skill_gaps = analyze_soft_skill_gaps(resume_text, job_desc)

    total_gap_penalty = 0
    if hard_skill_gaps:
        total_gap_penalty += 5
    if scope_gaps:
        total_gap_penalty += min(15, len(scope_gaps) * 5)
    if soft_skill_gaps:
        total_gap_penalty += min(10, len(soft_skill_gaps) * 3)

    experience_depth = estimate_project_depth(resume_text)
    achievements = count_quantified_achievements(resume_text)
    achievement_score = min(100, achievements * 10)

    overall = round(
        keyword_match_score * 0.45 +
        comm["overall"] * 0.20 +
        experience_depth * 0.15 +
        achievement_score * 0.10 -
        total_gap_penalty * 0.10
    )
    overall = max(0, min(100, overall))

    tip = _generate_jd_tip(matched, missing, comm, experience_depth, achievements, hard_skill_gaps, scope_gaps, soft_skill_gaps, get_domain_info(domain)["label"])

    return {
        "match_score": overall,
        "matched_keywords": sorted(matched),
        "missing_keywords": sorted(missing),
        "hard_skill_gaps": hard_skill_gaps,
        "scope_gaps": scope_gaps,
        "soft_skill_gaps": soft_skill_gaps,
        "improvement_tip": tip,
        "communication_score": comm["overall"],
        "experience_depth": experience_depth,
        "achievement_count": achievements,
        "domain": get_domain_info(domain)["label"],
        "domain_key": domain,
    }


def _path_without_jd(resume_text, comm, domain):
    domain_skills_list = get_domain_keywords(domain)
    domain_skills_set = set(domain_skills_list)
    resume_skills = extract_domain_skills(resume_text, domain)

    skills_density = len(resume_skills)
    max_domain_skills = len(domain_skills_list)
    skills_score = round((skills_density / max_domain_skills * 100)) if max_domain_skills > 0 else 0

    achievements = count_quantified_achievements(resume_text)
    achievement_score = min(100, achievements * 10)

    experience_depth = estimate_project_depth(resume_text)

    overall = round(
        skills_score * 0.25 +
        comm["overall"] * 0.25 +
        experience_depth * 0.30 +
        achievement_score * 0.20
    )
    overall = max(0, min(100, overall))

    missing_keywords = sorted(domain_skills_set - resume_skills)

    tip = _generate_standalone_tip(comm, skills_density, achievements, experience_depth, missing_keywords, get_domain_info(domain)["label"])

    return {
        "match_score": overall,
        "matched_keywords": sorted(resume_skills),
        "missing_keywords": missing_keywords[:15],
        "improvement_tip": tip,
        "communication_score": comm["overall"],
        "experience_depth": experience_depth,
        "achievement_count": achievements,
        "domain": get_domain_info(domain)["label"],
        "domain_key": domain,
    }


def _generate_jd_tip(matched, missing, comm, depth, achievements, hard_skill_gaps, scope_gaps, soft_skill_gaps, domain_label):
    parts = []
    if len(matched) < 3:
        parts.append(f"Your resume covers few {domain_label} keywords from the JD.")
    if hard_skill_gaps:
        top = hard_skill_gaps[:3]
        parts.append(f"Missing technical skills: {', '.join(top)}.")
    if scope_gaps:
        top = scope_gaps[:2]
        parts.append(f"Add experience at scale: {', '.join(top)}.")
    if soft_skill_gaps:
        top = soft_skill_gaps[:2]
        parts.append(f"Missing competencies: {', '.join(top)}.")
    if comm["overall"] < 70:
        parts.append("Improve written communication for a stronger impression.")
    if depth < 30:
        parts.append("Expand project descriptions with more detail about your contributions.")
    if achievements < 2:
        parts.append("Quantify accomplishments with metrics to stand out.")
    return " ".join(parts) if parts else "Your resume aligns well with this role!"


def _generate_standalone_tip(comm, skills_density, achievements, depth, missing, domain_label):
    parts = []
    if skills_density < 3:
        parts.append(f"Add more relevant {domain_label} skills to strengthen your profile.")
    if comm["overall"] < 70:
        parts.append("Improve clarity and professionalism in your writing.")
    if depth < 30:
        parts.append("Expand project descriptions to show deeper impact.")
    if achievements < 2:
        parts.append("Include quantifiable results (%, revenue, users) to demonstrate value.")
    if missing:
        top = missing[:3]
        parts.append(f"Consider building skills in: {', '.join(top)}.")
    return " ".join(parts) if parts else "Strong resume overall. Keep building!"
