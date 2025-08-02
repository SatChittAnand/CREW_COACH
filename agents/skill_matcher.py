from crewai import Agent

skill_matcher = Agent(
    role='Skill Matcher',
    goal='Map extracted skills to best-fit job roles and identify missing skills',
    backstory='An HR analyst with deep knowledge of skill-to-job role mapping',
    verbose=True
)
