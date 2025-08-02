from crewai import Agent

resume_analyzer = Agent(
    role='Resume Analyzer',
    goal='Analyze resume text to extract skills, experience, and education',
    backstory='An expert resume parsing assistant trained on thousands of resumes',
    verbose=True
)
