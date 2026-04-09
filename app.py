import streamlit as st

st.set_page_config(
    page_title="CareerCompass",
    page_icon="🧭",
    layout="centered"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
    
    * { font-family: 'Space Grotesk', sans-serif; }
    
    .main { background-color: #0a0a0f; }
    
    .stApp {
        background: #0a0a0f;
        color: #e0e0e0;
    }
    
    .hero {
        text-align: center;
        padding: 3rem 1rem 2rem;
    }
    
    .hero-badge {
        display: inline-block;
        background: rgba(99, 102, 241, 0.15);
        border: 1px solid rgba(99, 102, 241, 0.4);
        color: #a5b4fc;
        padding: 6px 18px;
        border-radius: 20px;
        font-size: 13px;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #e0e0ff 0%, #a5b4fc 50%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 1rem;
        line-height: 1.1;
    }
    
    .hero-sub {
        font-size: 1.1rem;
        color: #6b7280;
        margin-bottom: 2rem;
    }

    .section-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1.5rem;
    }
    
    .section-label {
        font-size: 11px;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #6366f1;
        margin-bottom: 0.5rem;
    }
    
    .question-text {
        font-size: 1.25rem;
        font-weight: 600;
        color: #f0f0ff;
        margin-bottom: 1.5rem;
        line-height: 1.5;
    }

    .progress-text {
        font-size: 13px;
        color: #4b5563;
        text-align: right;
        margin-bottom: 0.5rem;
    }

    .result-role {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #a5b4fc, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.5rem 0;
    }

    .result-desc {
        color: #9ca3af;
        font-size: 1rem;
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }

    .skill-badge {
        display: inline-block;
        background: rgba(99,102,241,0.12);
        border: 1px solid rgba(99,102,241,0.25);
        color: #a5b4fc;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 13px;
        margin: 3px;
    }

    .soft-badge {
        display: inline-block;
        background: rgba(16,185,129,0.1);
        border: 1px solid rgba(16,185,129,0.25);
        color: #6ee7b7;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 13px;
        margin: 3px;
    }

    .roadmap-item {
        display: flex;
        gap: 12px;
        padding: 12px 0;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }

    .coming-soon {
        text-align: center;
        padding: 4rem 2rem;
        color: #4b5563;
    }

    div[data-testid="stRadio"] label {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 12px !important;
        padding: 14px 18px !important;
        margin-bottom: 8px !important;
        cursor: pointer !important;
        transition: all 0.2s !important;
        color: #d1d5db !important;
        font-size: 15px !important;
        display: block !important;
        width: 100% !important;
    }

    div[data-testid="stRadio"] label:hover {
        border-color: rgba(99,102,241,0.5) !important;
        background: rgba(99,102,241,0.08) !important;
    }

    .stButton button {
        background: linear-gradient(135deg, #6366f1, #818cf8) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 32px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        width: 100% !important;
        cursor: pointer !important;
        transition: opacity 0.2s !important;
    }

    .stButton button:hover { opacity: 0.9 !important; }

    div[data-testid="stSelectbox"] > div {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 12px !important;
        color: #d1d5db !important;
    }

    h3 { color: #e0e0ff !important; font-weight: 600 !important; }
    
    .stProgress > div > div {
        background: linear-gradient(90deg, #6366f1, #818cf8) !important;
        border-radius: 4px !important;
    }
    
    .stProgress > div {
        background: rgba(255,255,255,0.05) !important;
        border-radius: 4px !important;
    }
</style>
""", unsafe_allow_html=True)

ROLES = {
    "Data Scientist": {
        "emoji": "🔬",
        "color": "#818cf8",
        "desc": "You love discovering hidden patterns and building models that predict the future. Math and experimentation are your superpowers.",
        "hard": ["Python (pandas, sklearn, tensorflow)", "Statistics & probability", "Machine Learning algorithms", "SQL", "Jupyter Notebook, Git"],
        "soft": ["Curiosity", "Critical thinking", "Patience", "Communication"],
        "courses": ["Machine Learning — Andrew Ng (Coursera)", "Fast.ai — Practical Deep Learning", "Kaggle Learn (free)"],
        "books": ["Hands-On Machine Learning — Géron", "The 100-Page ML Book — Burkov", "Thinking Fast and Slow — Kahneman"],
        "projects": ["Kaggle competition (any)", "Prediction model on real data", "NLP or Computer Vision project"]
    },
    "ML Engineer": {
        "emoji": "⚙️",
        "color": "#a78bfa",
        "desc": "You don't just build models — you make them work in the real world at scale. You bridge research and production.",
        "hard": ["Python (production level)", "PyTorch / TensorFlow", "MLOps — Docker, Kubernetes", "Cloud — AWS/GCP/Azure", "API development"],
        "soft": ["Engineering mindset", "Attention to detail", "Collaboration", "Problem solving under pressure"],
        "courses": ["MLOps Specialization — DeepLearning.AI", "Docker & Kubernetes — Udemy", "AWS/GCP free tier practice"],
        "books": ["Designing ML Systems — Chip Huyen", "Building ML Pipelines — Hapke"],
        "projects": ["Deploy ML model via FastAPI", "Build CI/CD pipeline for a model", "Real-time prediction API"]
    },
    "Data Analyst": {
        "emoji": "📊",
        "color": "#38bdf8",
        "desc": "You find the story hidden in the numbers. SQL is your language, and you love turning messy data into clear insights.",
        "hard": ["SQL — your main tool", "Python or R for analysis", "Tableau or Power BI", "Excel / Google Sheets", "Statistics basics"],
        "soft": ["Storytelling with data", "Curiosity", "Attention to detail", "Communication with non-technical people"],
        "courses": ["Google Data Analytics — Coursera ⭐", "SQL — Mode Analytics / SQLZoo", "Tableau / Power BI — YouTube"],
        "books": ["Storytelling with Data — Nussbaumer", "Lean Analytics — Croll & Yoskovitz", "Naked Statistics — Wheelan"],
        "projects": ["SQL analysis on real dataset", "Dashboard in Tableau/Power BI", "End-to-end analysis with insights"]
    },
    "BI Analyst": {
        "emoji": "📈",
        "color": "#34d399",
        "desc": "You build the reporting systems that entire companies rely on. You turn business questions into dashboards that executives trust.",
        "hard": ["SQL advanced", "Power BI or Tableau deeply", "Data modeling — star schema", "ETL basics", "Excel advanced"],
        "soft": ["Business understanding", "Structured thinking", "Stakeholder management", "Presentation skills"],
        "courses": ["Power BI — Microsoft Learn (free)", "SQL Advanced — DataCamp", "Data Modeling — dbt Learn (free)"],
        "books": ["The Data Warehouse Toolkit — Kimball", "Storytelling with Data — Nussbaumer"],
        "projects": ["Corporate dashboard in Power BI", "Star schema design", "Automated reporting system"]
    },
    "Product Analyst": {
        "emoji": "🎯",
        "color": "#fb923c",
        "desc": "You obsess over user behaviour. You run A/B tests, track funnels, and help product teams make decisions backed by data.",
        "hard": ["SQL", "Product metrics — DAU, MAU, Retention, Churn, LTV", "A/B testing", "Amplitude or Mixpanel", "Python basics"],
        "soft": ["Empathy for users", "Curiosity about human behaviour", "Hypothesis thinking", "Communication with product teams"],
        "courses": ["Amplitude Academy — free ⭐", "Google Data Analytics — Coursera", "A/B Testing — Udacity"],
        "books": ["Lean Analytics — Croll & Yoskovitz", "Hooked — Nir Eyal", "Cracking the PM Interview — McDowell"],
        "projects": ["Funnel analysis project", "A/B test simulation", "User behaviour dashboard"]
    },
    "Business Analyst": {
        "emoji": "💼",
        "color": "#fbbf24",
        "desc": "You are the bridge between business and technology. You listen, translate, and make sure the right problems get solved.",
        "hard": ["SQL basics", "Excel / Google Sheets advanced", "BPMN — process modelling", "Requirements writing", "Jira, Confluence"],
        "soft": ["Active listening", "Structured thinking", "Negotiation", "Stakeholder communication"],
        "courses": ["Business Analysis Fundamentals — Udemy", "IIBA Entry Certificate in BA", "SQL basics — SQLZoo"],
        "books": ["Business Analysis — Debra Paul", "The BA Handbook — Podeswa", "Thinking Fast and Slow — Kahneman"],
        "projects": ["Business case analysis of a real company", "Process mapping (BPMN diagram)", "Requirements document for an app"]
    },
    "Data Engineer": {
        "emoji": "🔧",
        "color": "#f472b6",
        "desc": "You build the infrastructure that makes everything else possible. Without you, there's no data to analyse or model to train.",
        "hard": ["Python (production level)", "SQL advanced", "ETL/ELT — Airflow, dbt", "Big Data — Spark", "Cloud + Docker + Kubernetes"],
        "soft": ["Systems thinking", "Reliability mindset", "Collaboration with DS and analysts", "Documentation"],
        "courses": ["Data Engineering Zoomcamp — free ⭐", "Apache Airflow — official docs", "dbt Learn — free"],
        "books": ["Fundamentals of Data Engineering — Joe Reis", "Designing Data-Intensive Applications — Kleppmann"],
        "projects": ["ETL pipeline with Airflow", "Data warehouse on BigQuery", "Real-time streaming pipeline"]
    }
}

QUESTIONS = [
    {
        "block": "PERSONALITY",
        "q": "When you face a new problem, what do you do first?",
        "options": [
            ("Break it into parts and analyze step by step", {"Data Scientist": 2, "Data Analyst": 1, "BI Analyst": 1}),
            ("Think about the system and architecture behind it", {"Data Engineer": 2, "ML Engineer": 2}),
            ("Talk to people to understand the real need", {"Business Analyst": 2, "Product Analyst": 1}),
            ("Start experimenting and testing hypotheses", {"Data Scientist": 1, "ML Engineer": 1, "Product Analyst": 2}),
        ]
    },
    {
        "block": "PERSONALITY",
        "q": "Which word describes you best?",
        "options": [
            ("Precise and mathematical", {"Data Scientist": 2, "ML Engineer": 1, "BI Analyst": 1}),
            ("Curious about human behaviour", {"Product Analyst": 2, "Business Analyst": 1}),
            ("Builder and systems thinker", {"Data Engineer": 2, "ML Engineer": 2}),
            ("Strategic and business-minded", {"Business Analyst": 2, "BI Analyst": 1}),
        ]
    },
    {
        "block": "PERSONALITY",
        "q": "You have a free weekend. What do you naturally do?",
        "options": [
            ("Learn a new algorithm or read a math paper", {"Data Scientist": 2, "ML Engineer": 1}),
            ("Build or automate something technical", {"Data Engineer": 2, "ML Engineer": 2}),
            ("Analyse trends — markets, apps, user behaviour", {"Product Analyst": 2, "Data Analyst": 1}),
            ("Plan, organise, create structure from chaos", {"Business Analyst": 2, "BI Analyst": 1}),
        ]
    },
    {
        "block": "PERSONALITY",
        "q": "What frustrates you most?",
        "options": [
            ("Messy, unreliable data that I can't trust", {"Data Engineer": 2, "Data Analyst": 1}),
            ("Models that work in research but fail in production", {"ML Engineer": 2, "Data Scientist": 1}),
            ("Decisions made without looking at the data", {"Business Analyst": 2, "BI Analyst": 1}),
            ("Not knowing why users are behaving a certain way", {"Product Analyst": 2, "Data Analyst": 1}),
        ]
    },
    {
        "block": "PERSONALITY",
        "q": "How do you make important decisions?",
        "options": [
            ("Deep analysis — I need data and statistical confidence", {"Data Scientist": 2, "Data Analyst": 1}),
            ("Experimentation — I test and measure results", {"ML Engineer": 1, "Product Analyst": 2}),
            ("Business context — what's the goal and who benefits?", {"Business Analyst": 2, "BI Analyst": 1}),
            ("System design — what's scalable and reliable?", {"Data Engineer": 2, "ML Engineer": 1}),
        ]
    },
    {
        "block": "INTERESTS",
        "q": "Which topic could you read about for hours?",
        "options": [
            ("How neural networks and AI algorithms learn", {"Data Scientist": 2, "ML Engineer": 2}),
            ("Why users behave the way they do in apps", {"Product Analyst": 2, "Business Analyst": 1}),
            ("How data flows through large-scale systems", {"Data Engineer": 2, "ML Engineer": 1}),
            ("How companies measure and improve performance", {"BI Analyst": 2, "Business Analyst": 1}),
        ]
    },
    {
        "block": "INTERESTS",
        "q": "Which article title grabs your attention immediately?",
        "options": [
            ("How Spotify's recommendation engine actually works", {"Data Scientist": 2, "ML Engineer": 1}),
            ("Why users abandon apps after day 3 — a data study", {"Product Analyst": 2, "Data Analyst": 1}),
            ("How to build a real-time data pipeline at scale", {"Data Engineer": 2, "ML Engineer": 1}),
            ("How Kaspi became Kazakhstan's super app — business breakdown", {"Business Analyst": 2, "BI Analyst": 1}),
        ]
    },
    {
        "block": "INTERESTS",
        "q": "What kind of result excites you the most?",
        "options": [
            ("A model with 94% accuracy deployed in production", {"ML Engineer": 2, "Data Scientist": 1}),
            ("Finding the hidden reason behind a metric drop", {"Data Analyst": 2, "Product Analyst": 1}),
            ("A dashboard that changed a major business decision", {"BI Analyst": 2, "Business Analyst": 1}),
            ("A pipeline that processes 1 million rows per second", {"Data Engineer": 2, "ML Engineer": 1}),
        ]
    },
    {
        "block": "INTERESTS",
        "q": "Which subject did you enjoy most in school?",
        "options": [
            ("Advanced math, statistics, probability", {"Data Scientist": 2, "ML Engineer": 1}),
            ("Psychology, sociology, economics", {"Product Analyst": 2, "Business Analyst": 1}),
            ("Computer science, programming, logic", {"Data Engineer": 2, "ML Engineer": 1}),
            ("Business, management, systems thinking", {"Business Analyst": 2, "BI Analyst": 2}),
        ]
    },
    {
        "block": "INTERESTS",
        "q": "If you had to pick one superpower at work, what would it be?",
        "options": [
            ("Predict the future with data", {"Data Scientist": 2, "ML Engineer": 1}),
            ("Understand what users truly want", {"Product Analyst": 2, "Business Analyst": 1}),
            ("Build systems that never break", {"Data Engineer": 2, "ML Engineer": 1}),
            ("Turn chaos into clear, beautiful reports", {"BI Analyst": 2, "Data Analyst": 1}),
        ]
    },
    {
        "block": "WORK STYLE",
        "q": "You get a new dataset. What's your first instinct?",
        "options": [
            ("Explore distributions, correlations, outliers", {"Data Scientist": 2, "Data Analyst": 1}),
            ("Ask — what business question does this answer?", {"Business Analyst": 2, "BI Analyst": 1}),
            ("Think about how to store and process it efficiently", {"Data Engineer": 2, "ML Engineer": 1}),
            ("Look for user behaviour patterns and product signals", {"Product Analyst": 2, "Data Analyst": 1}),
        ]
    },
    {
        "block": "WORK STYLE",
        "q": "You prefer working:",
        "options": [
            ("Alone with deep technical focus for hours", {"Data Scientist": 2, "Data Engineer": 1}),
            ("Closely with product and design teams", {"Product Analyst": 2, "Business Analyst": 1}),
            ("With engineers on infrastructure and systems", {"Data Engineer": 2, "ML Engineer": 2}),
            ("Presenting insights to leadership and stakeholders", {"BI Analyst": 2, "Business Analyst": 1}),
        ]
    },
    {
        "block": "WORK STYLE",
        "q": "When presenting your work, you naturally show:",
        "options": [
            ("Model performance metrics and technical details", {"Data Scientist": 2, "ML Engineer": 1}),
            ("User behaviour insights and product recommendations", {"Product Analyst": 2, "Data Analyst": 1}),
            ("System architecture and pipeline diagrams", {"Data Engineer": 2, "ML Engineer": 1}),
            ("Business KPIs, trends, and actionable next steps", {"BI Analyst": 2, "Business Analyst": 2}),
        ]
    },
    {
        "block": "WORK STYLE",
        "q": "Your biggest strength is:",
        "options": [
            ("Turning complex math into working models", {"Data Scientist": 2, "ML Engineer": 1}),
            ("Making data understandable for everyone", {"Data Analyst": 2, "BI Analyst": 1}),
            ("Building reliable systems that scale", {"Data Engineer": 2, "ML Engineer": 2}),
            ("Connecting data to real business decisions", {"Business Analyst": 2, "Product Analyst": 1}),
        ]
    },
    {
        "block": "WORK STYLE",
        "q": "How do you feel about writing code?",
        "options": [
            ("I love it — the more complex the better", {"Data Scientist": 1, "ML Engineer": 2, "Data Engineer": 2}),
            ("I use SQL and Python as tools for analysis", {"Data Analyst": 2, "Product Analyst": 1}),
            ("I prefer visual tools — dashboards and reports", {"BI Analyst": 2, "Business Analyst": 1}),
            ("I build production-grade code that runs at scale", {"Data Engineer": 2, "ML Engineer": 2}),
        ]
    },
    {
        "block": "KEY DIFFERENTIATORS",
        "q": "Data Scientist vs ML Engineer — which sounds more like you?",
        "options": [
            ("I love research, discovering new patterns, pure science", {"Data Scientist": 3}),
            ("I love building, deploying, scaling — engineering mindset", {"ML Engineer": 3}),
            ("I love finding insights and telling stories with data", {"Data Analyst": 2, "Product Analyst": 1}),
            ("I love designing systems that make data flow perfectly", {"Data Engineer": 3}),
        ]
    },
    {
        "block": "KEY DIFFERENTIATORS",
        "q": "Data Analyst vs BI Analyst — which fits you better?",
        "options": [
            ("Deep ad-hoc analysis — answer complex one-time questions", {"Data Analyst": 3}),
            ("Build standard dashboards the whole company uses daily", {"BI Analyst": 3}),
            ("Understand user behaviour and product metrics", {"Product Analyst": 3}),
            ("Bridge between business needs and data solutions", {"Business Analyst": 3}),
        ]
    },
    {
        "block": "KEY DIFFERENTIATORS",
        "q": "Which sentence feels MOST like you?",
        "options": [
            ("I want to discover patterns nobody has seen before", {"Data Scientist": 3}),
            ("I want to build AI systems that work in the real world", {"ML Engineer": 3}),
            ("I want to help businesses make smarter decisions", {"Business Analyst": 2, "BI Analyst": 1}),
            ("I want to build the data infrastructure everything runs on", {"Data Engineer": 3}),
        ]
    },
    {
        "block": "KEY DIFFERENTIATORS",
        "q": "A startup asks for your help. You naturally focus on:",
        "options": [
            ("Their ML models and prediction systems", {"Data Scientist": 2, "ML Engineer": 2}),
            ("Their key metrics — what do the numbers say?", {"Data Analyst": 2, "BI Analyst": 1}),
            ("Their users — who are they and what do they want?", {"Product Analyst": 3}),
            ("Their data infrastructure — how does data move?", {"Data Engineer": 3}),
        ]
    },
    {
        "block": "VISION",
        "q": "In 5 years, you want people to say about you:",
        "options": [
            ("They built models that changed how we predict things", {"Data Scientist": 2, "ML Engineer": 1}),
            ("They always found the insight that nobody else noticed", {"Data Analyst": 2, "Product Analyst": 1}),
            ("They made our data infrastructure bulletproof", {"Data Engineer": 3}),
            ("They made our business smarter with data", {"Business Analyst": 2, "BI Analyst": 1}),
        ]
    },
]

def init_state():
    if "stage" not in st.session_state:
        st.session_state.stage = "home"
    if "area" not in st.session_state:
        st.session_state.area = None
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
    if "scores" not in st.session_state:
        st.session_state.scores = {r: 0 for r in ROLES}
    if "answers" not in st.session_state:
        st.session_state.answers = {}

init_state()

# HOME
if st.session_state.stage == "home":
    st.markdown("""
    <div class="hero">
        <div class="hero-badge">🧭 Career Discovery Tool</div>
        <div class="hero-title">CareerCompass</div>
        <div class="hero-sub">20 questions. 7 data roles. Your personalized IT roadmap.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Step 1 — Choose your area</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-text">Which IT area are you exploring?</div>', unsafe_allow_html=True)

    area = st.radio("", [
        "📊  Data & Analytics",
        "💻  Development",
        "🏢  Management"
    ], label_visibility="collapsed")

    if st.button("Start the quiz →"):
        st.session_state.area = area
        if "Data" in area:
            st.session_state.stage = "quiz"
        else:
            st.session_state.stage = "coming_soon"
        st.rerun()

# COMING SOON
elif st.session_state.stage == "coming_soon":
    st.markdown("""
    <div class="hero">
        <div class="hero-title">Coming Soon</div>
        <div class="hero-sub">We're building this direction. Data & Analytics is ready now!</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center; padding: 2rem 0;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🚀</div>
        <div style="color: #6b7280; font-size: 1rem; line-height: 1.8;">
            Development and Management tracks are under construction.<br>
            Try <strong style="color: #a5b4fc;">Data & Analytics</strong> — it's fully ready!
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("← Go back"):
        st.session_state.stage = "home"
        st.rerun()

# QUIZ
elif st.session_state.stage == "quiz":
    idx = st.session_state.q_index
    total = len(QUESTIONS)
    q = QUESTIONS[idx]

    st.markdown(f'<div class="progress-text">Question {idx + 1} of {total}</div>', unsafe_allow_html=True)
    st.progress((idx + 1) / total)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="section-label">Block — {q["block"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="question-text">{q["q"]}</div>', unsafe_allow_html=True)

    options = [opt[0] for opt in q["options"]]
    key = f"q_{idx}"

    default = options.index(st.session_state.answers[idx]) if idx in st.session_state.answers else 0
    selected = st.radio("", options, index=default, label_visibility="collapsed", key=key)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if idx > 0:
            if st.button("← Back"):
                st.session_state.q_index -= 1
                st.rerun()
    with col2:
        btn_label = "See my result →" if idx == total - 1 else "Next →"
        if st.button(btn_label):
            st.session_state.answers[idx] = selected
            for opt_text, score_dict in q["options"]:
                if opt_text == selected:
                    for role, pts in score_dict.items():
                        st.session_state.scores[role] += pts
            if idx < total - 1:
                st.session_state.q_index += 1
                st.rerun()
            else:
                st.session_state.stage = "result"
                st.rerun()

# RESULT
elif st.session_state.stage == "result":
    scores = st.session_state.scores
    top_role = max(scores, key=scores.get)
    role = ROLES[top_role]

    st.markdown(f"""
    <div class="hero">
        <div class="hero-badge">✨ Your best match</div>
        <div style="font-size: 3rem; margin: 0.5rem 0;">{role['emoji']}</div>
        <div class="result-role">{top_role}</div>
        <div class="result-desc">{role['desc']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Score breakdown
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Score breakdown</div>', unsafe_allow_html=True)
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    max_score = sorted_scores[0][1] or 1
    for r, s in sorted_scores:
        pct = int(s / max_score * 100)
        emoji = ROLES[r]["emoji"]
        color = ROLES[r]["color"]
        st.markdown(f"""
        <div style="margin-bottom: 10px;">
            <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                <span style="color:#d1d5db; font-size:14px;">{emoji} {r}</span>
                <span style="color:{color}; font-size:14px; font-weight:600;">{pct}%</span>
            </div>
            <div style="background:rgba(255,255,255,0.05); border-radius:4px; height:6px;">
                <div style="background:{color}; width:{pct}%; height:6px; border-radius:4px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Skills
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-label">Hard skills to learn</div>', unsafe_allow_html=True)
        for s in role["hard"]:
            st.markdown(f'<span class="skill-badge">{s}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-label">Soft skills to develop</div>', unsafe_allow_html=True)
        for s in role["soft"]:
            st.markdown(f'<span class="soft-badge">{s}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Roadmap
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Your personalized roadmap</div>', unsafe_allow_html=True)

    st.markdown("**📚 Courses**")
    for i, c in enumerate(role["courses"], 1):
        st.markdown(f'<div style="color:#d1d5db; font-size:14px; padding:6px 0; border-bottom:1px solid rgba(255,255,255,0.05);">{"0"+str(i) if i<10 else i}. &nbsp; {c}</div>', unsafe_allow_html=True)

    st.markdown("<br>**📖 Books**")
    for i, b in enumerate(role["books"], 1):
        st.markdown(f'<div style="color:#d1d5db; font-size:14px; padding:6px 0; border-bottom:1px solid rgba(255,255,255,0.05);">{"0"+str(i) if i<10 else i}. &nbsp; {b}</div>', unsafe_allow_html=True)

    st.markdown("<br>**🛠 Projects to build**")
    for i, p in enumerate(role["projects"], 1):
        st.markdown(f'<div style="color:#d1d5db; font-size:14px; padding:6px 0; border-bottom:1px solid rgba(255,255,255,0.05);">{"0"+str(i) if i<10 else i}. &nbsp; {p}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔄 Retake the quiz"):
        st.session_state.stage = "home"
        st.session_state.q_index = 0
        st.session_state.scores = {r: 0 for r in ROLES}
        st.session_state.answers = {}
        st.rerun()
