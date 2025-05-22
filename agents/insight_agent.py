from crewai import Agent

class InsightAgent:
    def __init__(self):
        self.agent = Agent(
            name="InsightAgent",
            role="Summarizes insights",
            goal="Provide final sentiment breakdown",
            backstory="You are an insights strategist. Based on processed sentiment and trend data, you generate summaries and actionable conclusions that can influence business and product decisions."
        )

    def run(self, sentiments):
        from collections import Counter
        count = Counter([s["label"] for s in sentiments])
        return dict(count)