import re

DOMAINS = {
    "fashion": {
        "label": "Fashion & Design",
        "detect": [
            "fashion", "textile", "garment", "apparel", "runway", "couture",
            "sketching", "draping", "pattern making", "sewing", "tailoring",
            "merchandising", "wardrobe", "stylist", "couturier", "embroidery",
            "prints", "silhouette", "collection", "lookbook", "trend forecasting",
        ],
        "skills": [
            "sketching", "draping", "pattern making", "textiles", "sewing",
            "tailoring", "embroidery", "garment construction", "fashion illustration",
            "trend analysis", "color theory", "fabric selection", "merchandising",
            "styling", "lookbook creation", "fashion marketing", "retail",
            "photoshop", "illustrator", "coral draw", "clo 3d", "marvelous designer",
            "fashion design", "apparel design", "technical design", "fitting",
        ],
        "jobs": {
            "Fashion Designer": {
                "skills": [
                    "sketching", "draping", "pattern making", "garment construction",
                    "fashion illustration", "trend analysis", "color theory",
                    "fabric selection", "styling", "lookbook creation",
                    "textiles", "sewing", "fashion design", "apparel design",
                    "photoshop", "illustrator", "collection", "silhouette",
                ],
            },
            "Textile Designer": {
                "skills": [
                    "textiles", "fabric selection", "embroidery", "prints",
                    "color theory", "pattern making", "sketching",
                    "trend analysis", "illustrator", "photoshop",
                    "garment construction", "weaving", "dyeing",
                ],
            },
            "Fashion Stylist": {
                "skills": [
                    "styling", "wardrobe", "trend analysis", "color theory",
                    "lookbook creation", "fashion marketing", "photoshop",
                    "branding", "visual merchandising", "fashion",
                ],
            },
            "Pattern Maker": {
                "skills": [
                    "pattern making", "draping", "sewing", "garment construction",
                    "technical design", "fitting", "textiles", "sketching",
                    "clo 3d", "marvelous designer", "tailoring",
                ],
            },
            "Merchandiser": {
                "skills": [
                    "merchandising", "retail", "fashion marketing", "trend analysis",
                    "branding", "visual merchandising", "buying", "inventory management",
                    "sales analysis", "product development",
                ],
            },
            "Fashion Illustrator": {
                "skills": [
                    "fashion illustration", "sketching", "color theory",
                    "photoshop", "illustrator", "digital art",
                    "drawing", "painting", "visual communication",
                ],
            },
            "Creative Director": {
                "skills": [
                    "creative direction", "brand strategy", "art direction",
                    "trend forecasting", "team leadership", "campaign management",
                    "visual merchandising", "styling", "photoshop", "illustrator",
                ],
            },
            "Product Development Manager": {
                "skills": [
                    "product development", "garment construction", "textiles",
                    "fitting", "technical design", "vendor management",
                    "production management", "quality control", "sourcing",
                ],
            },
            "Fashion Buyer": {
                "skills": [
                    "buying", "merchandising", "trend analysis", "negotiation",
                    "vendor management", "inventory management", "retail",
                    "market research", "budgeting", "forecasting",
                ],
            },
            "Visual Merchandiser": {
                "skills": [
                    "visual merchandising", "retail", "styling", "display design",
                    "branding", "photoshop", "illustrator", "trend analysis",
                    "creative direction", "window display",
                ],
            },
        },
    },
    "software": {
        "label": "Software Engineering",
        "detect": [
            "software", "developer", "engineer", "programming", "code",
            "frontend", "backend", "full stack", "api", "algorithm",
            "github", "agile", "scrum", "sprint", "deploy",
        ],
        "skills": [
            "python", "java", "javascript", "typescript", "c++", "c#", "ruby", "go", "rust",
            "sql", "nosql", "mongodb", "postgresql", "mysql", "redis",
            "react", "angular", "vue", "django", "flask", "spring", "node", "express",
            "docker", "kubernetes", "aws", "gcp", "azure", "ci/cd", "jenkins",
            "git", "linux", "rest api", "graphql", "microservices",
            "html", "css", "bootstrap", "tailwind", "nextjs",
            "oop", "data structures", "algorithms", "design patterns",
            "tdd", "unit testing", "jest", "pytest",
        ],
        "jobs": {
            "Software Engineer": {
                "skills": [
                    "python", "java", "javascript", "sql", "git", "oop",
                    "data structures", "algorithms", "design patterns",
                    "agile", "tdd", "rest api", "linux", "debugging",
                ],
            },
            "Frontend Developer": {
                "skills": [
                    "javascript", "typescript", "react", "angular", "vue",
                    "html", "css", "bootstrap", "tailwind", "nextjs",
                    "git", "rest api", "webpack", "figma", "responsive design",
                ],
            },
            "Backend Developer": {
                "skills": [
                    "python", "java", "node", "sql", "postgresql", "mongodb",
                    "rest api", "graphql", "docker", "aws", "git",
                    "microservices", "redis", "express", "django", "flask",
                ],
            },
            "Full Stack Developer": {
                "skills": [
                    "javascript", "react", "angular", "node", "python",
                    "sql", "mongodb", "rest api", "html", "css",
                    "git", "docker", "aws", "express", "django",
                ],
            },
            "DevOps Engineer": {
                "skills": [
                    "docker", "kubernetes", "aws", "gcp", "azure",
                    "ci/cd", "jenkins", "terraform", "ansible", "linux",
                    "git", "bash", "monitoring", "nginx", "helm",
                ],
            },
            "Mobile Developer": {
                "skills": [
                    "swift", "kotlin", "react native", "flutter", "android",
                    "ios", "javascript", "typescript", "rest api", "git",
                    "mobile ui", "app store", "google play",
                ],
            },
            "Tech Lead": {
                "skills": [
                    "system design", "microservices", "cloud", "leadership",
                    "agile", "code review", "mentoring", "architecture",
                    "project management", "stakeholder management",
                ],
            },
            "Systems Architect": {
                "skills": [
                    "system design", "microservices", "cloud", "kubernetes",
                    "aws", "architecture", "scalability", "security",
                    "distributed systems", "design patterns", "mongodb",
                ],
            },
            "QA Engineer": {
                "skills": [
                    "tdd", "unit testing", "integration testing", "jest",
                    "pytest", "cypress", "selenium", "playwright",
                    "automation", "bug tracking", "agile", "jira",
                ],
            },
        },
    },
    "marketing": {
        "label": "Marketing & Digital Media",
        "detect": [
            "marketing", "seo", "sem", "content", "brand", "social media",
            "campaign", "digital marketing", "ppc", "analytics",
            "growth", "conversion", "audience", "funnel",
        ],
        "skills": [
            "seo", "sem", "ppc", "google analytics", "google ads", "facebook ads",
            "content marketing", "social media", "email marketing", "marketing automation",
            "hubspot", "salesforce", "mailchimp", "hootsuite", "buffer",
            "copywriting", "a/b testing", "crm", "lead generation", "brand strategy",
            "market research", "keyword research", "analytics", "reporting",
            "photoshop", "canva", "wordpress", "figma",
        ],
        "jobs": {
            "Digital Marketing Manager": {
                "skills": [
                    "digital marketing", "seo", "sem", "social media",
                    "content marketing", "email marketing", "analytics",
                    "google analytics", "campaign management", "budgeting",
                    "lead generation", "brand strategy", "reporting",
                ],
            },
            "SEO Specialist": {
                "skills": [
                    "seo", "keyword research", "google analytics", "sem",
                    "content marketing", "link building", "analytics",
                    "wordpress", "reporting", "search console",
                ],
            },
            "Content Marketer": {
                "skills": [
                    "content marketing", "copywriting", "seo", "blogging",
                    "social media", "email marketing", "storytelling",
                    "wordpress", "analytics", "brand strategy",
                ],
            },
            "Social Media Manager": {
                "skills": [
                    "social media", "content marketing", "facebook ads",
                    "instagram", "linkedin", "twitter", "analytics",
                    "hootsuite", "buffer", "brand strategy", "canva",
                ],
            },
            "PPC Analyst": {
                "skills": [
                    "ppc", "google ads", "facebook ads", "sem",
                    "analytics", "a/b testing", "keyword research",
                    "google analytics", "reporting", "budget management",
                ],
            },
            "Brand Manager": {
                "skills": [
                    "brand strategy", "marketing", "market research",
                    "campaign management", "social media", "content marketing",
                    "analytics", "creative direction", "branding",
                ],
            },
            "Marketing Analyst": {
                "skills": [
                    "analytics", "google analytics", "data analysis",
                    "reporting", "market research", "seo", "excel",
                    "tableau", "a/b testing", "campaign analysis",
                ],
            },
            "Growth Hacker": {
                "skills": [
                    "growth", "a/b testing", "analytics", "seo", "ppc",
                    "email marketing", "conversion", "product marketing",
                    "data analysis", "automation", "crm",
                ],
            },
            "Email Marketing Specialist": {
                "skills": [
                    "email marketing", "mailchimp", "automation",
                    "copywriting", "analytics", "a/b testing", "crm",
                    "lead generation", "reporting", "campaign management",
                ],
            },
        },
    },
    "finance": {
        "label": "Finance & Accounting",
        "detect": [
            "finance", "accounting", "audit", "tax", "financial", "investment",
            "budget", "forecast", "revenue", "balance sheet", "p&l",
            "compliance", "risk management", "portfolio",
        ],
        "skills": [
            "financial modeling", "forecasting", "budgeting", "variance analysis",
            "quickbooks", "xero", "sap", "oracle financials", "excel",
            "power bi", "tableau", "risk assessment", "auditing", "tax preparation",
            "gaap", "ifrs", "financial reporting", "reconciliation",
            "cost analysis", "profitability analysis", "cash flow management",
        ],
        "jobs": {
            "Financial Analyst": {
                "skills": [
                    "financial modeling", "forecasting", "budgeting",
                    "variance analysis", "excel", "financial reporting",
                    "gaap", "power bi", "data analysis", "valuation",
                ],
            },
            "Accountant": {
                "skills": [
                    "accounting", "gaap", "reconciliation", "quickbooks",
                    "xero", "excel", "financial reporting", "tax preparation",
                    "auditing", "accounts payable", "accounts receivable",
                ],
            },
            "Auditor": {
                "skills": [
                    "auditing", "risk assessment", "compliance", "gaap",
                    "internal controls", "financial reporting", "excel",
                    "data analysis", "ifrs", "reconciliation",
                ],
            },
            "Tax Specialist": {
                "skills": [
                    "tax preparation", "tax planning", "compliance",
                    "gaap", "financial reporting", "research",
                    "accounting", "excel", "tax software",
                ],
            },
            "Financial Manager": {
                "skills": [
                    "financial reporting", "budgeting", "forecasting",
                    "financial modeling", "risk management", "leadership",
                    "gaap", "excel", "cash flow management", "p&l",
                ],
            },
            "Investment Banker": {
                "skills": [
                    "valuation", "financial modeling", "mergers",
                    "acquisitions", "deal structuring", "due diligence",
                    "forecasting", "excel", "presentation",
                ],
            },
            "Risk Analyst": {
                "skills": [
                    "risk assessment", "risk management", "compliance",
                    "data analysis", "financial modeling", "forecasting",
                    "excel", "reporting", "power bi",
                ],
            },
            "CFO": {
                "skills": [
                    "financial strategy", "budgeting", "forecasting",
                    "cash flow management", "risk management", "leadership",
                    "gaap", "financial reporting", "p&l", "board reporting",
                ],
            },
            "Budget Analyst": {
                "skills": [
                    "budgeting", "forecasting", "variance analysis",
                    "financial reporting", "excel", "cost analysis",
                    "data analysis", "reporting", "financial modeling",
                ],
            },
            "Compliance Officer": {
                "skills": [
                    "compliance", "risk management", "regulatory",
                    "auditing", "policy development", "training",
                    "reporting", "investigation", "legal research",
                ],
            },
        },
    },
    "healthcare": {
        "label": "Healthcare & Medical",
        "detect": [
            "healthcare", "medical", "clinical", "patient", "hospital",
            "nurse", "doctor", "pharmacy", "diagnosis", "treatment",
            "surgery", "therapist", "rehabilitation",
        ],
        "skills": [
            "patient care", "clinical research", "medical records", "ehr", "epic",
            "diagnosis", "treatment planning", "surgery", "pharmacology",
            "anatomy", "physiology", "pathology", "radiology",
            "cpr", "bls", "acls", "hipaa", "medical coding",
            "healthcare management", "telemedicine", "public health",
        ],
        "jobs": {
            "Registered Nurse": {
                "skills": [
                    "patient care", "cpr", "bls", "acls", "ehr",
                    "clinical assessment", "care planning", "medication administration",
                    "vital signs", "patient education", "hipaa",
                ],
            },
            "Physician": {
                "skills": [
                    "diagnosis", "treatment planning", "patient care",
                    "surgery", "anatomy", "physiology", "pathology",
                    "medical records", "clinical research", "pharmacology",
                ],
            },
            "Medical Assistant": {
                "skills": [
                    "patient care", "vital signs", "ehr", "medical records",
                    "clinical procedures", "hipaa", "scheduling",
                    "phlebotomy", "insurance verification",
                ],
            },
            "Healthcare Administrator": {
                "skills": [
                    "healthcare management", "hospital administration",
                    "budgeting", "compliance", "hipaa", "leadership",
                    "policy development", "staff management", "operations",
                ],
            },
            "Clinical Researcher": {
                "skills": [
                    "clinical research", "data analysis", "trial management",
                    "hipaa", "regulatory compliance", "medical writing",
                    "statistics", "patient recruitment", "protocol development",
                ],
            },
            "Pharmacist": {
                "skills": [
                    "pharmacology", "medication management", "patient counseling",
                    "prescription verification", "clinical pharmacy",
                    "drug interactions", "inventory management", "hipaa",
                ],
            },
            "Physical Therapist": {
                "skills": [
                    "rehabilitation", "patient care", "treatment planning",
                    "anatomy", "physiology", "exercise prescription",
                    "manual therapy", "patient education", "evaluation",
                ],
            },
            "Medical Coder": {
                "skills": [
                    "medical coding", "icd-10", "cpt", "hipaa",
                    "medical records", "reimbursement", "auditing",
                    "compliance", "ehr", "billing",
                ],
            },
            "Health Informatics Specialist": {
                "skills": [
                    "ehr", "epic", "healthcare data", "data analysis",
                    "hipaa", "clinical systems", "project management",
                    "training", "workflow optimization", "reporting",
                ],
            },
        },
    },
    "education": {
        "label": "Education & Academia",
        "detect": [
            "education", "teaching", "curriculum", "academic", "professor",
            "instructor", "lecturer", "student", "research", "pedagogy",
            "classroom", "lesson", "syllabus",
        ],
        "skills": [
            "curriculum development", "lesson planning", "classroom management",
            "educational technology", "assessment", "differentiated instruction",
            "student counseling", "e-learning", "moodle", "blackboard",
            "research methodology", "grant writing", "publication",
            "mentoring", "online teaching", "k-12", "higher education",
        ],
        "jobs": {
            "Teacher": {
                "skills": [
                    "lesson planning", "classroom management", "assessment",
                    "differentiated instruction", "curriculum development",
                    "student engagement", "parent communication", "grading",
                ],
            },
            "Professor": {
                "skills": [
                    "teaching", "research", "publication", "curriculum development",
                    "mentoring", "grant writing", "lecturing", "student advising",
                    "research methodology", "academic writing",
                ],
            },
            "Curriculum Developer": {
                "skills": [
                    "curriculum development", "instructional design",
                    "educational technology", "assessment design",
                    "lesson planning", "e-learning", "moodle", "blackboard",
                ],
            },
            "Educational Consultant": {
                "skills": [
                    "education policy", "curriculum development",
                    "teacher training", "assessment", "program evaluation",
                    "strategic planning", "professional development",
                ],
            },
            "Instructional Designer": {
                "skills": [
                    "instructional design", "e-learning", "educational technology",
                    "curriculum development", "moodle", "blackboard",
                    "multimedia", "assessment design", "authoring tools",
                ],
            },
            "Academic Advisor": {
                "skills": [
                    "student counseling", "academic planning", "mentoring",
                    "career guidance", "student development", "advising",
                    "higher education", "registration",
                ],
            },
            "School Administrator": {
                "skills": [
                    "school administration", "staff management", "budgeting",
                    "policy development", "parent communication",
                    "curriculum oversight", "strategic planning",
                ],
            },
            "Researcher": {
                "skills": [
                    "research", "data analysis", "publication",
                    "research methodology", "grant writing", "statistics",
                    "literature review", "academic writing", "presentation",
                ],
            },
            "E-learning Specialist": {
                "skills": [
                    "e-learning", "educational technology", "moodle",
                    "blackboard", "instructional design", "multimedia",
                    "authoring tools", "lms administration", "training",
                ],
            },
            "Education Coordinator": {
                "skills": [
                    "program coordination", "curriculum development",
                    "teacher training", "assessment", "student services",
                    "event planning", "budgeting", "reporting",
                ],
            },
        },
    },
    "business": {
        "label": "Business & Management",
        "detect": [
            "business", "management", "strategy", "consulting", "operations",
            "project management", "stakeholder", "business development",
            "process improvement", "six sigma", "lean",
        ],
        "skills": [
            "project management", "business strategy", "operations management",
            "process optimization", "six sigma", "lean", "agile",
            "stakeholder management", "risk management", "change management",
            "microsoft project", "jira", "confluence", "visio",
            "p&l management", "vendor management", "negotiation",
            "business analysis", "requirements gathering", "kpi tracking",
        ],
        "jobs": {
            "Business Analyst": {
                "skills": [
                    "business analysis", "requirements gathering", "data analysis",
                    "stakeholder management", "process improvement",
                    "agile", "jira", "confluence", "documentation",
                ],
            },
            "Project Manager": {
                "skills": [
                    "project management", "agile", "scrum", "stakeholder management",
                    "risk management", "budgeting", "scheduling",
                    "jira", "microsoft project", "team leadership",
                ],
            },
            "Management Consultant": {
                "skills": [
                    "business strategy", "process optimization", "data analysis",
                    "stakeholder management", "change management",
                    "financial modeling", "presentation", "market research",
                ],
            },
            "Operations Manager": {
                "skills": [
                    "operations management", "process improvement",
                    "six sigma", "lean", "supply chain", "budgeting",
                    "team leadership", "kpi tracking", "vendor management",
                ],
            },
            "Product Manager": {
                "skills": [
                    "product strategy", "roadmap planning", "agile",
                    "stakeholder management", "user research", "analytics",
                    "a/b testing", "jira", "cross-functional leadership",
                ],
            },
            "Program Manager": {
                "skills": [
                    "program management", "project management", "agile",
                    "risk management", "stakeholder management", "budgeting",
                    "cross-functional coordination", "reporting",
                ],
            },
            "Business Development Manager": {
                "skills": [
                    "business development", "sales strategy", "negotiation",
                    "client relationship", "market research", "partnerships",
                    "lead generation", "presentation", "contract negotiation",
                ],
            },
            "Strategy Manager": {
                "skills": [
                    "business strategy", "market research", "data analysis",
                    "competitive analysis", "financial modeling",
                    "strategic planning", "presentation", "leadership",
                ],
            },
        },
    },
    "creative": {
        "label": "Creative Arts & Media",
        "detect": [
            "graphic design", "illustration", "animation", "photography",
            "video editing", "motion graphics", "creative", "art",
            "visual", "multimedia", "adobe",
        ],
        "skills": [
            "photoshop", "illustrator", "indesign", "after effects", "premiere pro",
            "figma", "sketch", "blender", "maya", "cinema 4d",
            "typography", "color theory", "composition", "branding",
            "motion graphics", "video production", "photography",
            "ui design", "ux design", "wireframing", "prototyping",
        ],
        "jobs": {
            "Graphic Designer": {
                "skills": [
                    "photoshop", "illustrator", "indesign", "typography",
                    "color theory", "composition", "branding", "layout",
                    "logo design", "print design", "creativity",
                ],
            },
            "UI/UX Designer": {
                "skills": [
                    "ui design", "ux design", "wireframing", "prototyping",
                    "figma", "sketch", "user research", "usability testing",
                    "interaction design", "visual design", "information architecture",
                ],
            },
            "Art Director": {
                "skills": [
                    "art direction", "creative direction", "branding",
                    "visual design", "photoshop", "illustrator",
                    "team leadership", "campaign management", "photography",
                ],
            },
            "Motion Graphics Designer": {
                "skills": [
                    "motion graphics", "after effects", "animation",
                    "premiere pro", "cinema 4d", "blender",
                    "video production", "typography", "illustrator",
                ],
            },
            "Video Editor": {
                "skills": [
                    "video editing", "premiere pro", "after effects",
                    "final cut pro", "color grading", "audio editing",
                    "storytelling", "motion graphics", "production",
                ],
            },
            "Photographer": {
                "skills": [
                    "photography", "lighting", "composition", "editing",
                    "photoshop", "lightroom", "portrait", "commercial",
                    "retouching", "studio management",
                ],
            },
            "Illustrator": {
                "skills": [
                    "illustration", "drawing", "painting", "photoshop",
                    "illustrator", "digital art", "color theory",
                    "composition", "character design", "storyboarding",
                ],
            },
            "Creative Director": {
                "skills": [
                    "creative direction", "brand strategy", "art direction",
                    "team leadership", "campaign management", "visual design",
                    "creative strategy", "client management", "budgeting",
                ],
            },
            "Brand Designer": {
                "skills": [
                    "branding", "logo design", "visual identity",
                    "typography", "color theory", "illustrator",
                    "photoshop", "brand strategy", "packaging design",
                ],
            },
            "Multimedia Specialist": {
                "skills": [
                    "multimedia", "photoshop", "illustrator", "premiere pro",
                    "after effects", "animation", "video production",
                    "web design", "photography", "motion graphics",
                ],
            },
            "Animator": {
                "skills": [
                    "animation", "blender", "maya", "cinema 4d",
                    "after effects", "storyboarding", "character design",
                    "3d modeling", "rigging", "texturing",
                ],
            },
        },
    },
    "data": {
        "label": "Data & Analytics",
        "detect": [
            "data science", "data analysis", "data engineer", "analytics",
            "machine learning", "statistics", "prediction", "visualization",
            "pandas", "numpy", "sql", "python",
        ],
        "skills": [
            "python", "r", "sql", "pandas", "numpy", "scikit-learn",
            "tensorflow", "pytorch", "machine learning", "deep learning",
            "statistics", "hypothesis testing", "a/b testing",
            "tableau", "power bi", "looker", "matplotlib", "seaborn",
            "spark", "hadoop", "airflow", "data wrangling",
            "feature engineering", "model deployment", "etl",
        ],
        "jobs": {
            "Data Scientist": {
                "skills": [
                    "python", "r", "sql", "machine learning", "statistics",
                    "pandas", "scikit-learn", "tensorflow", "pytorch",
                    "data wrangling", "feature engineering", "visualization",
                    "a/b testing", "hypothesis testing",
                ],
            },
            "Data Analyst": {
                "skills": [
                    "sql", "excel", "python", "r", "tableau", "power bi",
                    "data analysis", "statistics", "visualization",
                    "reporting", "pandas", "a/b testing",
                ],
            },
            "Data Engineer": {
                "skills": [
                    "python", "sql", "spark", "airflow", "etl",
                    "data warehousing", "aws", "kafka", "hadoop",
                    "postgresql", "mongodb", "data modeling",
                ],
            },
            "Machine Learning Engineer": {
                "skills": [
                    "python", "machine learning", "deep learning",
                    "tensorflow", "pytorch", "scikit-learn", "mlops",
                    "model deployment", "docker", "aws", "sql",
                ],
            },
            "BI Analyst": {
                "skills": [
                    "tableau", "power bi", "sql", "data analysis",
                    "reporting", "dashboard", "excel", "visualization",
                    "business intelligence", "kpi tracking",
                ],
            },
            "Quantitative Analyst": {
                "skills": [
                    "python", "r", "statistics", "financial modeling",
                    "machine learning", "mathematics", "data analysis",
                    "sql", "excel", "risk modeling",
                ],
            },
            "AI Engineer": {
                "skills": [
                    "python", "machine learning", "deep learning",
                    "tensorflow", "pytorch", "nlp", "computer vision",
                    "model deployment", "docker", "aws",
                ],
            },
            "Research Scientist": {
                "skills": [
                    "research", "machine learning", "deep learning",
                    "python", "statistics", "publication",
                    "experimental design", "data analysis", "pytorch",
                ],
            },
            "Analytics Manager": {
                "skills": [
                    "analytics", "data analysis", "team leadership",
                    "sql", "tableau", "power bi", "reporting",
                    "stakeholder management", "strategy",
                ],
            },
        },
    },
    "sales": {
        "label": "Sales & Customer Service",
        "detect": [
            "sales", "account management", "customer success", "b2b",
            "revenue", "lead generation", "client relationship",
            "business development", "salesforce", "cold calling",
        ],
        "skills": [
            "salesforce", "hubspot", "crm", "lead generation", "cold calling",
            "account management", "negotiation", "closing", "forecasting",
            "customer success", "onboarding", "upselling", "cross-selling",
            "sales strategy", "territory management", "pipeline management",
        ],
        "jobs": {
            "Sales Representative": {
                "skills": [
                    "sales", "cold calling", "lead generation", "negotiation",
                    "closing", "crm", "salesforce", "pipeline management",
                    "product knowledge", "presentation",
                ],
            },
            "Account Executive": {
                "skills": [
                    "sales", "account management", "lead generation",
                    "negotiation", "closing", "crm", "salesforce",
                    "forecasting", "pipeline management", "b2b",
                ],
            },
            "Sales Manager": {
                "skills": [
                    "sales strategy", "team management", "forecasting",
                    "pipeline management", "coaching", "crm",
                    "salesforce", "territory management", "reporting",
                ],
            },
            "Customer Success Manager": {
                "skills": [
                    "customer success", "onboarding", "account management",
                    "upselling", "cross-selling", "crm", "training",
                    "client relationship", "retention", "support",
                ],
            },
            "Business Development Representative": {
                "skills": [
                    "business development", "lead generation", "cold calling",
                    "prospecting", "crm", "salesforce", "outreach",
                    "qualification", "pipeline building",
                ],
            },
            "Account Manager": {
                "skills": [
                    "account management", "client relationship", "upselling",
                    "cross-selling", "crm", "salesforce", "negotiation",
                    "contract renewal", "customer satisfaction",
                ],
            },
            "Sales Operations Analyst": {
                "skills": [
                    "sales operations", "analytics", "forecasting",
                    "crm", "salesforce", "reporting", "data analysis",
                    "pipeline management", "process improvement",
                ],
            },
            "Regional Sales Manager": {
                "skills": [
                    "sales management", "territory management", "forecasting",
                    "team leadership", "budgeting", "crm", "salesforce",
                    "strategic planning", "partner management",
                ],
            },
        },
    },
    "hr": {
        "label": "Human Resources",
        "detect": [
            "human resources", "recruiting", "talent", "onboarding", "hiring",
            "payroll", "employee relations", "compensation", "benefits",
            "hrbp", "people operations", "workforce",
        ],
        "skills": [
            "recruiting", "onboarding", "payroll", "benefits administration",
            "employee relations", "performance management", "training",
            "hr policies", "compliance", "labor law", "workday", "successfactors",
            "talent acquisition", "sourcing", "interviewing", "offer negotiation",
        ],
        "jobs": {
            "HR Manager": {
                "skills": [
                    "hr management", "employee relations", "performance management",
                    "recruiting", "onboarding", "compliance", "labor law",
                    "hr policies", "benefits administration", "leadership",
                ],
            },
            "Recruiter": {
                "skills": [
                    "recruiting", "sourcing", "interviewing", "talent acquisition",
                    "offer negotiation", "onboarding", "crm", "linkedin",
                    "applicant tracking", "job postings",
                ],
            },
            "Talent Acquisition Specialist": {
                "skills": [
                    "talent acquisition", "recruiting", "sourcing",
                    "interviewing", "employer branding", "crm",
                    "offer negotiation", "market research", "hiring strategy",
                ],
            },
            "HR Business Partner": {
                "skills": [
                    "hr business partner", "employee relations",
                    "performance management", "talent management",
                    "organizational development", "coaching",
                    "change management", "strategic planning",
                ],
            },
            "Compensation Analyst": {
                "skills": [
                    "compensation", "benefits administration", "market analysis",
                    "job evaluation", "excel", "data analysis",
                    "reporting", "hr policies", "benchmarking",
                ],
            },
            "Training Coordinator": {
                "skills": [
                    "training", "onboarding", "employee development",
                    "program coordination", "learning management",
                    "presentation", "curriculum development", "assessment",
                ],
            },
            "Payroll Specialist": {
                "skills": [
                    "payroll", "benefits administration", "compliance",
                    "tax filing", "time tracking", "hr software",
                    "reporting", "auditing", "labor law",
                ],
            },
            "People Operations Manager": {
                "skills": [
                    "people operations", "employee experience", "hr operations",
                    "process improvement", "data analysis", "hr technology",
                    "compliance", "onboarding", "employee relations",
                ],
            },
        },
    },
    "legal": {
        "label": "Legal",
        "detect": [
            "legal", "law", "attorney", "lawyer", "paralegal", "litigation",
            "corporate law", "compliance", "contract", "intellectual property",
            "legal research", "court", "legal counsel",
        ],
        "skills": [
            "legal research", "contract drafting", "negotiation", "litigation",
            "corporate law", "intellectual property", "compliance",
            "legal writing", "case management", "discovery", "deposition",
            "westlaw", "lexisnexis", "document review", "risk assessment",
        ],
        "jobs": {
            "Lawyer": {
                "skills": [
                    "legal research", "legal writing", "litigation",
                    "negotiation", "client counseling", "trial advocacy",
                    "case management", "contract drafting", "deposition",
                ],
            },
            "Paralegal": {
                "skills": [
                    "legal research", "case management", "document review",
                    "discovery", "legal writing", "westlaw", "lexisnexis",
                    "filing", "trial preparation", "client communication",
                ],
            },
            "Legal Counsel": {
                "skills": [
                    "corporate law", "contract drafting", "negotiation",
                    "legal research", "compliance", "risk management",
                    "legal writing", "advisory", "policy development",
                ],
            },
            "Compliance Officer": {
                "skills": [
                    "compliance", "risk management", "regulatory",
                    "policy development", "auditing", "training",
                    "investigation", "reporting", "legal research",
                ],
            },
            "Corporate Attorney": {
                "skills": [
                    "corporate law", "contract drafting", "mergers",
                    "acquisitions", "negotiation", "legal research",
                    "due diligence", "governance", "securities law",
                ],
            },
            "Legal Analyst": {
                "skills": [
                    "legal research", "legal writing", "data analysis",
                    "document review", "compliance", "reporting",
                    "case analysis", "westlaw", "lexisnexis",
                ],
            },
            "Contract Manager": {
                "skills": [
                    "contract drafting", "contract management", "negotiation",
                    "legal research", "compliance", "risk assessment",
                    "document review", "vendor management", "clm software",
                ],
            },
            "Intellectual Property Specialist": {
                "skills": [
                    "intellectual property", "patent", "trademark",
                    "copyright", "legal research", "prosecution",
                    "licensing", "litigation support", "ip strategy",
                ],
            },
            "Litigation Associate": {
                "skills": [
                    "litigation", "legal research", "legal writing",
                    "discovery", "deposition", "trial preparation",
                    "motion practice", "case management", "client communication",
                ],
            },
        },
    },
    "hospitality": {
        "label": "Hospitality & Tourism",
        "detect": [
            "hospitality", "hotel", "tourism", "restaurant", "travel",
            "guest", "concierge", "catering", "event planning", "resort",
        ],
        "skills": [
            "hotel management", "guest services", "event planning", "catering",
            "travel planning", "tour operations", "revenue management",
            "property management", "pms", "opera", "reservations",
            "food safety", "wine knowledge", "hospitality management",
        ],
        "jobs": {
            "Hotel Manager": {
                "skills": [
                    "hotel management", "guest services", "revenue management",
                    "staff management", "budgeting", "pms", "opera",
                    "reservations", "hospitality", "operations",
                ],
            },
            "Event Coordinator": {
                "skills": [
                    "event planning", "catering", "guest services",
                    "vendor management", "budgeting", "coordination",
                    "hospitality", "decor", "timeline management",
                ],
            },
            "Travel Consultant": {
                "skills": [
                    "travel planning", "tourism", "customer service",
                    "booking", "destination knowledge", "sales",
                    "itinerary planning", "cruise", "airline",
                ],
            },
            "Restaurant Manager": {
                "skills": [
                    "restaurant management", "guest services", "food safety",
                    "inventory management", "staff training", "budgeting",
                    "wine knowledge", "hospitality", "operations",
                ],
            },
            "Concierge": {
                "skills": [
                    "concierge", "guest services", "hospitality",
                    "communication", "local knowledge", "problem solving",
                    "booking", "recommendations", "customer service",
                ],
            },
            "Tour Guide": {
                "skills": [
                    "tourism", "travel", "storytelling", "local history",
                    "customer service", "tour planning", "communication",
                    "group management", "multilingual",
                ],
            },
            "Hospitality Director": {
                "skills": [
                    "hospitality management", "hotel operations",
                    "strategic planning", "revenue management", "team leadership",
                    "guest services", "budgeting", "property management",
                ],
            },
            "Guest Relations Manager": {
                "skills": [
                    "guest services", "hospitality", "customer service",
                    "complaint resolution", "communication", "team management",
                    "pms", "opera", "experience management",
                ],
            },
            "Reservations Manager": {
                "skills": [
                    "reservations", "pms", "opera", "revenue management",
                    "guest services", "team management", "forecasting",
                    "reporting", "distribution channels",
                ],
            },
            "Banquet Manager": {
                "skills": [
                    "banquet", "catering", "event planning", "food safety",
                    "staff management", "guest services", "budgeting",
                    "setup", "hospitality", "coordination",
                ],
            },
        },
    },
    "engineering": {
        "label": "Engineering (Mechanical, Civil, Electrical)",
        "detect": [
            "mechanical engineering", "civil engineering", "electrical engineering",
            "cad", "autocad", "solidworks", "manufacturing", "structural",
            "circuit", "mep", "construction", "mechatronics",
        ],
        "skills": [
            "autocad", "solidworks", "revit", "catia", "ansys", "matlab",
            "structural analysis", "mechanical design", "civil 3d",
            "project management", "p&id", "plc", "scada", "embedded systems",
            "manufacturing", "quality control", "lean manufacturing",
            "thermodynamics", "fluid mechanics", "circuit design",
        ],
        "jobs": {
            "Mechanical Engineer": {
                "skills": [
                    "mechanical design", "solidworks", "catia", "ansys",
                    "thermodynamics", "fluid mechanics", "manufacturing",
                    "cad", "matlab", "p&id", "quality control",
                ],
            },
            "Civil Engineer": {
                "skills": [
                    "civil engineering", "autocad", "revit", "civil 3d",
                    "structural analysis", "construction", "project management",
                    "surveying", "mep", "site management",
                ],
            },
            "Electrical Engineer": {
                "skills": [
                    "electrical engineering", "circuit design", "plc",
                    "scada", "embedded systems", "matlab", "autocad",
                    "power systems", "p&id", "mep",
                ],
            },
            "Project Engineer": {
                "skills": [
                    "project management", "engineering", "autocad",
                    "solidworks", "budgeting", "scheduling",
                    "quality control", "vendor management", "reporting",
                ],
            },
            "Design Engineer": {
                "skills": [
                    "design", "cad", "solidworks", "autocad", "catia",
                    "mechanical design", "structural analysis", "prototyping",
                    "finite element analysis", "product development",
                ],
            },
            "Manufacturing Engineer": {
                "skills": [
                    "manufacturing", "lean manufacturing", "quality control",
                    "process improvement", "cad", "solidworks",
                    "production", "six sigma", "automation",
                ],
            },
            "Structural Engineer": {
                "skills": [
                    "structural analysis", "autocad", "revit",
                    "civil engineering", "construction", "steel design",
                    "concrete design", "ansys", "building codes",
                ],
            },
            "CAD Designer": {
                "skills": [
                    "cad", "autocad", "solidworks", "revit", "catia",
                    "drafting", "3d modeling", "technical drawing",
                    "blueprint", "detailing",
                ],
            },
            "Quality Engineer": {
                "skills": [
                    "quality control", "six sigma", "lean manufacturing",
                    "process improvement", "inspection", "auditing",
                    "iso", "root cause analysis", "statistical analysis",
                ],
            },
        },
    },
    "content": {
        "label": "Content Writing & Journalism",
        "detect": [
            "writing", "journalism", "content", "editor", "copywriter",
            "blog", "article", "published", "storytelling", "editorial",
            "news", "media", "publication", "freelance writing",
        ],
        "skills": [
            "copywriting", "editing", "proofreading", "research",
            "seo writing", "content strategy", "storytelling", "feature writing",
            "news reporting", "interviewing", "fact-checking",
            "wordpress", "grammarly", "google docs", "ap style",
            "creative writing", "technical writing", "blogging",
        ],
        "jobs": {
            "Content Writer": {
                "skills": [
                    "writing", "editing", "proofreading", "research",
                    "seo writing", "blogging", "wordpress", "storytelling",
                    "grammarly", "content strategy",
                ],
            },
            "Copywriter": {
                "skills": [
                    "copywriting", "advertising", "brand voice",
                    "editing", "proofreading", "research", "creative writing",
                    "marketing", "persuasive writing", "storytelling",
                ],
            },
            "Journalist": {
                "skills": [
                    "journalism", "news reporting", "interviewing",
                    "fact-checking", "feature writing", "editing",
                    "research", "ap style", "storytelling", "deadline",
                ],
            },
            "Editor": {
                "skills": [
                    "editing", "proofreading", "writing", "fact-checking",
                    "ap style", "content strategy", "team management",
                    "grammar", "copy editing", "publication",
                ],
            },
            "Technical Writer": {
                "skills": [
                    "technical writing", "documentation", "editing",
                    "research", "api documentation", "user guides",
                    "simplification", "technical concepts", "google docs",
                ],
            },
            "Blog Manager": {
                "skills": [
                    "blogging", "content strategy", "seo writing",
                    "editing", "wordpress", "analytics", "social media",
                    "editorial calendar", "team management",
                ],
            },
            "Content Strategist": {
                "skills": [
                    "content strategy", "seo", "analytics", "editorial planning",
                    "brand voice", "market research", "writing",
                    "social media", "content marketing", "reporting",
                ],
            },
            "News Reporter": {
                "skills": [
                    "news reporting", "journalism", "interviewing",
                    "investigation", "fact-checking", "writing",
                    "deadline", "ap style", "broadcast", "multimedia",
                ],
            },
            "SEO Writer": {
                "skills": [
                    "seo writing", "keyword research", "blogging",
                    "editing", "wordpress", "analytics", "content strategy",
                    "research", "html basics", "search console",
                ],
            },
            "Creative Writer": {
                "skills": [
                    "creative writing", "storytelling", "fiction",
                    "editing", "proofreading", "research",
                    "narrative", "dialogue", "character development",
                ],
            },
        },
    },
}

SENIORITY_KEYWORDS = {
    "junior": "Junior", "entry": "Junior", "fresher": "Junior",
    "senior": "Senior", "lead": "Lead", "principal": "Principal",
    "staff": "Staff", "head of": "Head of", "manager": "Manager",
    "director": "Director", "vp": "VP", "chief": "Chief",
}


def detect_domain(resume_text):
    text_lower = resume_text.lower()
    scores = {}
    for domain_key, domain_data in DOMAINS.items():
        score = 0
        for kw in domain_data["detect"]:
            if re.search(r'(?<!\w)' + re.escape(kw) + r'(?!\w)', text_lower):
                score += 1
        if score > 0:
            scores[domain_key] = score
    if not scores:
        return "business"
    return max(scores, key=scores.get)


def get_domain_info(domain):
    if domain not in DOMAINS:
        domain = "business"
    return DOMAINS[domain]


def get_domain_keywords(domain):
    if domain not in DOMAINS:
        domain = "business"
    return DOMAINS[domain]["skills"]


def get_all_skills():
    all_skills = set()
    for domain in DOMAINS.values():
        all_skills.update(domain["skills"])
    return all_skills


def get_domain_jobs(domain):
    if domain not in DOMAINS:
        domain = "business"
    return list(DOMAINS[domain]["jobs"].keys())


def get_job_skills(domain, job_title):
    if domain not in DOMAINS:
        domain = "business"
    jobs = DOMAINS[domain]["jobs"]
    if job_title in jobs:
        return jobs[job_title]["skills"]
    return get_domain_keywords(domain)


def extract_domain_skills(text, domain=None):
    text_lower = text.lower()
    skills = set()
    if domain:
        for kw in get_domain_keywords(domain):
            pattern = r'(?<!\w)' + re.escape(kw) + r'(?!\w)'
            if re.search(pattern, text_lower):
                skills.add(kw)
    else:
        for kw in get_all_skills():
            pattern = r'(?<!\w)' + re.escape(kw) + r'(?!\w)'
            if re.search(pattern, text_lower):
                skills.add(kw)
    return skills


def detect_seniority(text_lower):
    scores = {}
    for keyword, level in SENIORITY_KEYWORDS.items():
        if keyword in text_lower:
            scores[level] = scores.get(level, 0) + 1
    if scores:
        return max(scores, key=scores.get)
    years_match = re.findall(r'(\d+)\+?\s*years?', text_lower)
    if years_match:
        max_years = max(int(y) for y in years_match)
        if max_years >= 10:
            return "Senior"
        elif max_years >= 5:
            return "Mid-Level"
        elif max_years >= 2:
            return "Junior"
    return ""
