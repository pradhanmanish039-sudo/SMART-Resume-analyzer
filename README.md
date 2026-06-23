# 🧠 Smart Resume Analyzer

The **Smart Resume Analyzer** is an intelligent web application designed to help job seekers optimize their resumes for modern hiring systems.

Most companies use **Applicant Tracking Systems (ATS)** to filter resumes before human review. If resumes lack proper keywords or structure, they get rejected — even if the candidate has potential.

👉 This tool bridges the gap between your **resume** and your **target job role** using **data-driven analysis**.

---

## 🚀 Key Features

* 📊 ATS Compatibility Scoring
* 🔍 Keyword Matching Engine
* 🧠 Gap Analysis (GapLens)
* 🔄 Reverse ATS Matching

---

## ⚠️ Important Note

❌ No external AI/LLM APIs used
✅ Fully built using **local NLP + heuristic logic**

---

# 🔄 Full Workflow of the Website

## 🧩 Step-by-Step Flow

### 1️⃣ User Input

* Upload resume (PDF/DOCX)
* Enter job description (optional)

---

### 2️⃣ Text Extraction

* Extract resume text using parsing libraries
* Clean and preprocess data

---

### 3️⃣ Domain Detection

* Keyword frequency matching
* Maps resume to one of 15 domains

---

### 4️⃣ ATS Score Calculation

```bash
Score = (Matched Skills / Total Skills) × 100
```

* Uses set intersection
* Clamped between **5% – 100%**

---

### 5️⃣ Communication Score

* Based on readability metrics (textstat)
* Checks clarity, grammar, professionalism

---

### 6️⃣ Gap Analysis (GapLens)

* Uses regex pattern matching
* Detects missing skills from JD

---

### 7️⃣ Reverse ATS Matching

* Iterates through domain jobs
* Matches skills using regex
* Calculates scores
* Returns top 10 jobs

---

### 8️⃣ UI Rendering

* Uses `st.session_state`
* Toggle button → “See Job Options”
* Displays job title + confidence %

---

### 9️⃣ Final Output

* ATS Score
* Communication Score
* Missing Skills
* Suggestions
* Recommended Jobs

---

## 📊 Workflow Summary

| Step             | Process        | Technique        |
| ---------------- | -------------- | ---------------- |
| Input            | Resume + JD    | Upload           |
| Extraction       | Text parsing   | PyPDF            |
| Domain Detection | Keyword match  | Frequency        |
| Scoring          | Skill matching | Set intersection |
| Gap Analysis     | Missing skills | Regex            |
| Recommendation   | Job scoring    | Matching logic   |
| Output           | UI display     | Streamlit        |

---

## 💻 Code Flow

| File             | Function         | Role          |
| ---------------- | ---------------- | ------------- |
| recommender.py   | recommend_jobs() | Job scoring   |
| app.py (line 80) | Store results    | Session state |
| app.py (234–237) | Toggle button    | UI control    |
| app.py (283–293) | Render jobs      | Display       |

---

## ⚙️ Installation Guide

```bash
git clone https://github.com/pradhanmanish039-sudo/SMART-Resume-analyzer.git
cd SMART-Resume-analyzer
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Website Link

👉 https://smart-resume-analyzer-fgnwcihlbymtxnv68gmhul.streamlit.app/

---

## 🎥 Demo Video

👉 https://youtu.be/ofTcvb9fGAE

---

## 🧩 Tech Stack

| Category | Technology              |
| -------- | ----------------------- |
| Frontend | Streamlit               |
| Backend  | Python                  |
| NLP      | Keyword Matching, Regex |
| Parsing  | PyPDF                   |

---

## ⚠️ Challenges Faced

* Resume format variations
* Regex matching accuracy
* UI state management
* Deployment issues

---

## 📚 Lessons Learned

* ATS system understanding
* Rule-based NLP design
* Streamlit deployment
* Debugging real-world issues

---

## 🎯 Conclusion

This project proves that even without external AI APIs, a system can:

* ✔ Analyze resumes effectively
* ✔ Provide meaningful insights
* ✔ Suggest job roles
* ✔ Improve job selection chances

👉 It clearly shows how the system differentiates between strong and weak resumes.

---

