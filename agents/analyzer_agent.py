from crewai import Agent
from tools.sentiment_model import analyze_sentiment

class AnalyzerAgent:
    def __init__(self):
        self.agent = Agent(
            name="AnalyzerAgent",
            role="Performs sentiment analysis",
            goal="Generate polarity score",
            backstory="You are a sentiment and trend analyst powered by machine learning. You extract emotional tone, sentiment scores, and trends from structured or cleaned text to help businesses understand market signals."
        )

    def run(self, texts):
        return [analyze_sentiment(t) for t in texts]