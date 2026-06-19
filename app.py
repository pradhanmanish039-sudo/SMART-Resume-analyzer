import streamlit as st
import json
from utils.file_parser import extract_text
from utils.nlp import evaluate_communication
from utils.scorer import calculate_score
from utils.recommender import recommend_jobs
from utils.domain import detect_domain, get_domain_info

st.set_page_config(page_title="Smart Resume Analyser", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "show_jobs" not in st.session_state:
    st.session_state.show_jobs = False
if "results" not in st.session_state:
    st.session_state.results = None
if "jobs" not in st.session_state:
    st.session_state.jobs = None

st.markdown("""
<div class="brand-header">
    <h1>Smart Resume Analyser</h1>
    <p class="tagline">Upload your resume to get AI-powered ATS insights &amp; job recommendations</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="card-grid">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="card-label">📄 Upload Your Resume</p>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Drag and drop your resume here or click to upload (PDF or DOCX only)",
        type=["pdf", "docx"],
        label_visibility="collapsed",
    )
    st.markdown('<p class="formats-hint">Only PDF and DOCX formats are supported. Image files such as JPG, JPEG, and PNG are not allowed.</p>', unsafe_allow_html=True)

    if uploaded_file:
        if not uploaded_file.name.lower().endswith((".pdf", ".docx")):
            st.error("❌ Invalid file type! Please upload only PDF or DOCX files.")
        else:
            st.success("✅ Resume uploaded successfully! Preview is shown below.")
            st.markdown("### 👁️ Resume Preview")
            try:
                preview_text = extract_text(uploaded_file)
                st.text_area("Preview", preview_text[:800] + ("..." if len(preview_text) > 800 else ""), height=180, label_visibility="collapsed", disabled=True)
            except Exception:
                st.info("Preview available after analysis.")

    analyze_btn = st.button("Upload & Analyze", type="primary", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="card-label">Job Description <span class="optional">(Optional)</span></p>', unsafe_allow_html=True)
    job_desc = st.text_area("Paste job description", height=200, label_visibility="collapsed", placeholder="Paste job description here to check ATS match...")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

if analyze_btn and uploaded_file:
    with st.spinner("🔍 Analyzing your resume... Please wait."):
        try:
            resume_text = extract_text(uploaded_file)
        except Exception as e:
            st.error(f"❌ Invalid file type! Please upload only PDF or DOCX files.")
            st.stop()

        if not resume_text or len(resume_text.strip()) < 20:
            st.error("Extracted text is too short. Try a different file format.")
            st.stop()

        comm = evaluate_communication(resume_text)
        results = calculate_score(resume_text, job_desc if job_desc.strip() else None, comm)
        jobs = recommend_jobs(resume_text)

        st.session_state.results = results
        st.session_state.comm = comm
        st.session_state.jobs = jobs

    st.success("🎯 Analysis complete! Check your results below.")

if st.session_state.get("results"):
    data = st.session_state.results
    comm = st.session_state.get("comm", {})

    score = data["match_score"]
    has_jd = bool(job_desc and job_desc.strip())
    domain_label = data.get("domain", "General")
    domain_key = data.get("domain_key", "business")

    if has_jd:
        st.markdown(f"<h2 style='font-size:1.3rem;color:var(--navy);margin-bottom:1rem;'>ATS Match Results</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='font-size:1.3rem;color:var(--navy);margin-bottom:1rem;'>Resume Strength Results</h2>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align:center;margin-bottom:1.25rem;">
        <span style="background:#1a2744;color:white;padding:0.3rem 1rem;border-radius:20px;font-size:0.8rem;font-weight:600;">
            Detected Domain: {domain_label}
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="metric-grid">', unsafe_allow_html=True)

    mcol1, mcol2, mcol3 = st.columns(3)
    with mcol1:
        st.markdown(f"""
        <div class="metric-card metric-primary">
            <div class="metric-value">{score}%</div>
            <div class="metric-label">{'ATS Match Score' if has_jd else 'Resume Strength'}</div>
        </div>
        """, unsafe_allow_html=True)

    with mcol2:
        st.markdown(f"""
        <div class="metric-card { 'metric-green' if data.get('communication_score', 0) >= 70 else 'metric-amber' }">
            <div class="metric-value">{data.get('communication_score', 0)}%</div>
            <div class="metric-label">Communication</div>
        </div>
        """, unsafe_allow_html=True)

    with mcol3:
        st.markdown(f"""
        <div class="metric-card metric-green">
            <div class="metric-value">{data.get('achievement_count', 0)}</div>
            <div class="metric-label">Quantified Achievements</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-grid">', unsafe_allow_html=True)
    rcol1, rcol2 = st.columns(2)

    with rcol1:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:#065f46;'>✓ Matched Keywords ({len(data['matched_keywords'])})</h3>", unsafe_allow_html=True)
        if data["matched_keywords"]:
            tags = "".join(f'<span class="keyword-tag match">{kw}</span>' for kw in data["matched_keywords"])
            st.markdown(f'<div class="keyword-grid">{tags}</div>', unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:var(--gray-500);font-size:0.85rem;'>No keywords matched yet.</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with rcol2:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:#991b1b;'>✗ Missing Keywords ({len(data['missing_keywords'])})</h3>", unsafe_allow_html=True)
        if data["missing_keywords"]:
            tags = "".join(f'<span class="keyword-tag missing">{kw}</span>' for kw in data["missing_keywords"][:20])
            st.markdown(f'<div class="keyword-grid">{tags}</div>', unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:var(--gray-500);font-size:0.85rem;'>No missing keywords.</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if has_jd:
        st.markdown("<h3 style='font-size:1rem;color:var(--navy);margin:1rem 0 0.75rem;'>Gap Analysis</h3>", unsafe_allow_html=True)
        st.markdown('<div class="card-grid">', unsafe_allow_html=True)
        gcol1, gcol2, gcol3 = st.columns(3)

        with gcol1:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("<h3 style='color:#991b1b;'>🛠 Hard Skill Gaps</h3>", unsafe_allow_html=True)
            if data.get("hard_skill_gaps"):
                tags = "".join(f'<span class="keyword-tag missing">{kw}</span>' for kw in data["hard_skill_gaps"][:12])
                st.markdown(f'<div class="keyword-grid">{tags}</div>', unsafe_allow_html=True)
            else:
                st.markdown("<p style='color:var(--gray-500);font-size:0.85rem;'>No hard skill gaps detected.</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with gcol2:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("<h3 style='color:#991b1b;'>🌐 Scope & Scale Gaps</h3>", unsafe_allow_html=True)
            if data.get("scope_gaps"):
                tags = "".join(f'<span class="keyword-tag missing">{kw}</span>' for kw in data["scope_gaps"])
                st.markdown(f'<div class="keyword-grid">{tags}</div>', unsafe_allow_html=True)
            else:
                st.markdown("<p style='color:var(--gray-500);font-size:0.85rem;'>No scope gaps detected.</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with gcol3:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("<h3 style='color:#991b1b;'>👥 Soft Skill Gaps</h3>", unsafe_allow_html=True)
            if data.get("soft_skill_gaps"):
                tags = "".join(f'<span class="keyword-tag missing">{kw}</span>' for kw in data["soft_skill_gaps"])
                st.markdown(f'<div class="keyword-grid">{tags}</div>', unsafe_allow_html=True)
            else:
                st.markdown("<p style='color:var(--gray-500);font-size:0.85rem;'>No soft skill gaps detected.</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="tip-box">
        <strong>Improvement Tip</strong>
        {data['improvement_tip']}
    </div>
    """, unsafe_allow_html=True)

    if comm:
        st.markdown("<h3 style='font-size:1rem;color:var(--navy);margin-top:1.5rem;margin-bottom:0.75rem;'>Communication Skills Breakdown</h3>", unsafe_allow_html=True)
        st.markdown('<div class="comm-grid">', unsafe_allow_html=True)
        ccol1, ccol2, ccol3, ccol4 = st.columns(4)
        items = [
            ("Clarity", comm.get("clarity", 0)),
            ("Vocabulary", comm.get("vocabulary", 0)),
            ("Professionalism", comm.get("professionalism", 0)),
            ("Grammar", comm.get("grammar", 0)),
        ]
        cols = [ccol1, ccol2, ccol3, ccol4]
        for col, (label, val) in zip(cols, items):
            with col:
                st.markdown(f"""
                <div class="comm-item">
                    <div class="comm-value">{val}%</div>
                    <div class="comm-label">{label}</div>
                </div>
                """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        if comm.get("details"):
            st.markdown(f"<p style='font-size:0.85rem;color:var(--gray-700);'>{comm['details']}</p>", unsafe_allow_html=True)

st.markdown("""
<div class="floating-btn-container">
""", unsafe_allow_html=True)
job_btn_cols = st.columns([5, 1])
with job_btn_cols[1]:
    if st.button("See Job Options", key="floating_job_btn"):
        st.session_state.show_jobs = not st.session_state.show_jobs
st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.get("show_jobs") and st.session_state.get("jobs"):
    st.markdown("""
    <style>
    .jobs-section {
        background: #ffffff;
        border-radius: 16px;
        padding: 1.5rem 1.75rem;
        box-shadow: 0 8px 30px rgba(0,0,0,0.10);
        border: 1px solid #f0ebe3;
        margin: 1.5rem 0;
    }
    .jobs-section .jobs-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 1rem;
    }
    .jobs-section .jobs-header h2 {
        font-size: 1.2rem;
        font-weight: 700;
        color: #1a2744;
        margin: 0;
    }
    .jobs-section .jobs-sub {
        color: #888;
        font-size: 0.85rem;
        margin-bottom: 1.25rem;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="jobs-section">', unsafe_allow_html=True)

    hcol1, hcol2 = st.columns([8, 1])
    with hcol1:
        st.markdown("## Recommended Job Options")
    with hcol2:
        if st.button("✖", key="close_jobs_btn"):
            st.session_state.show_jobs = False
            st.rerun()

    st.markdown("Based on your resume skills and experience")

    for job in st.session_state.jobs:
        conf = job["confidence"]
        jcol1, jcol2 = st.columns([3, 1])
        with jcol1:
            st.markdown(f"**{job['title']}**")
        with jcol2:
            if conf >= 50:
                st.markdown(f"<p style='text-align:right;color:#2d6a4f;font-weight:700;margin:0;'>{conf}% match</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p style='text-align:right;color:#d97706;font-weight:700;margin:0;'>{conf}% match</p>", unsafe_allow_html=True)
        st.markdown("<hr style='margin:0.4rem 0;border:none;border-top:1px solid #f0ebe3;'>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.get("show_jobs") and not st.session_state.get("jobs"):
    st.markdown("""
    <style>
    .jobs-section {
        background: #ffffff;
        border-radius: 16px;
        padding: 1.5rem 1.75rem;
        box-shadow: 0 8px 30px rgba(0,0,0,0.10);
        border: 1px solid #f0ebe3;
        margin: 1.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="jobs-section">', unsafe_allow_html=True)
    hcol1, hcol2 = st.columns([8, 1])
    with hcol1:
        st.markdown("## Recommended Job Options")
    with hcol2:
        if st.button("✖", key="close_empty_btn"):
            st.session_state.show_jobs = False
            st.rerun()
    st.markdown("Upload your resume first to see job recommendations.")
    st.markdown('</div>', unsafe_allow_html=True)
