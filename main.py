from crewai import Crew, Task
from agents.resume_analyzer import resume_analyzer
from agents.skill_matcher import skill_matcher
from agents.job_market_scanner import job_market_scanner
from agents.career_recommender import career_recommender

# Step 1: Define your task
resume_task = Task(
    description=(
        "Analyze the following resume text:\n"
        "Name: Aryan Patel\n"
        "Education: B.Tech in Computer Science\n"
        "Skills: Python, JavaScript, React, SQL, Machine Learning\n"
        "Experience: 2 years as a full-stack developer at TechNova Pvt Ltd\n\n"
        "Extract key skills, match with suitable job roles, identify skill gaps, "
        "and recommend relevant career development steps."
    ),
    expected_output="A summary of suitable job roles, skill gaps, and course suggestions.",
    agent=career_recommender  # or whichever agent you want to lead this task
)

# Step 2: Create your crew
crew = Crew(
    agents=[
        resume_analyzer,
        skill_matcher,
        job_market_scanner,
        career_recommender
    ],
    tasks=[resume_task],
    verbose=True
)

# Step 3: Run the crew
output = crew.kickoff()
print("🧠 Final Recommendation:\n", output)
