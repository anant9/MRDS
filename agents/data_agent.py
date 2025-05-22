from crewai import Agent
from tools.twitter_scraper import fetch_tweets

class DataAgent:
    def __init__(self):
        self.agent = Agent(
            name="DataAgent",
            role="Extracts market data from Twitter and files",
            goal="Get relevant text data",
            backstory="You are a data extraction expert who specializes in collecting real-time insights from platforms like Twitter, Reddit, and CSV sources. Your goal is to find relevant raw content for market analysis."
        )

    def run(self, topic):
        return fetch_tweets(topic)