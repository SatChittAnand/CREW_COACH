# 🧠 Personalized Career Coach (CrewAI-Powered)

A smart, agent-based AI system built using [CrewAI](https://docs.crewai.com/) that helps users evaluate their resumes, identify suitable career paths, highlight skill gaps, and recommend relevant courses to grow professionally.

---

## 🚀 Features

- 📄 **Resume Analyzer**: Parses resumes to extract key skills, education, and experience.
- 🧩 **Skill Matcher**: Matches extracted skills with industry-relevant job roles.
- 🌐 **Job Market Scanner**: Evaluates current market trends to align skills with demand.
- 🧭 **Career Recommender**: Suggests suitable job roles, identifies gaps, and recommends personalized courses from Coursera, Udemy, edX, etc.

---

## 🛠️ Tech Stack

- 💬 [CrewAI](https://github.com/joaomdmoura/crewAI): Multi-agent orchestration
- 🤖 OpenAI GPT (via [LiteLLM](https://github.com/BerriAI/litellm)): LLM backend
- 🐍 Python 3.11+
- 📦 `python-dotenv`, `openai`, `crewai`, `litellm`

---

## 📁 Project Structure

```

crew\_coach/
│
├── main.py                          # Main runner script
├── .env                             # Contains your OpenAI API key
│
├── agents/
│   ├── resume\_analyzer.py          # Extracts skills, experience, education
│   ├── skill\_matcher.py            # Maps resume skills to roles
│   ├── job\_market\_scanner.py       # Scans trends for high-demand roles
│   └── career\_recommender.py       # Generates final recommendations
│
└── README.md

````

---

## 🧪 How It Works

1. Add your resume details to the `resume_text` in `main.py`.
2. Run the script:
   ```bash
   python main.py


3. The agents collaboratively analyze and return:

   * 🔎 Extracted skills
   * 💼 Suitable roles
   * 📉 Skill gaps
   * 🎓 Suggested online courses

---

## 🔐 Setup Instructions

### 1. Clone and Set Up Environment

```bash
git clone https://github.com/SatChittAnand/CREW_COACH.git
cd CREW_COACH
python -m venv venv
.\venv\Scripts\activate    # or source venv/bin/activate (Linux/macOS)
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, manually install:

```bash
pip install openai python-dotenv crewai litellm
```

### 3. Add Your OpenAI API Key

Create a `.env` file in the root folder:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 📦 Example Output

```
🧠 Final Recommendation:

Key Skills:
- Python, React, SQL, Machine Learning

Suitable Job Roles:
- Full-Stack Developer
- Data Scientist
- Software Engineer

Skill Gaps:
- Cloud (AWS, Azure)
- DevOps (Docker, CI/CD)
- Soft Skills (Communication)

Recommended Courses: (for eg: )
- "Applied Data Science with Python" (Coursera)
- "AWS Certified Architect" (Udemy)
- "Docker Mastery" (Udemy)
```

---

## 🌍 Future Improvements

* Upload PDF resumes for parsing
* Integration with real-time job APIs (Indeed, LinkedIn)
* UI using Streamlit or Gradio
* PDF export of final recommendations

---

## 📄 License

MIT License. © 2025 SatChittAnand

---

## 🤝 Contributing

PRs and suggestions are welcome. Please open an issue for discussion first.

---

## 💬 Contact

For queries or collaboration:

* 📧 [Email](mailto:satyanarayanmohanty177@gmail.com)
* 💼 [LinkedIn](https://www.linkedin.com/in/satyanarayan-mohanty-9a8466311/)


