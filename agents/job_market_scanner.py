from crewai import Agent

job_market_scanner = Agent(
    role='Job Market Scanner',
    goal='Analyze current job market trends and popular roles in demand',
    backstory='A job market analyst scanning global trends and in-demand technologies',
    verbose=True
)
