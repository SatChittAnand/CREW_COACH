from crewai import Agent

career_recommender = Agent(
    role='Career Recommender',
    goal='Suggest 3 best career paths and relevant courses to close skill gaps',
    backstory='A career guidance expert who recommends personalized learning paths',
    verbose=True
)
