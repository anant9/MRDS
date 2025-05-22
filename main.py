from agents.data_agent import DataAgent
from agents.cleaner_agent import CleanerAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.insight_agent import InsightAgent

def run_mrds(topic="Samsung Galaxy S24"):
    data_agent = DataAgent()
    cleaner_agent = CleanerAgent()
    analyzer_agent = AnalyzerAgent()
    insight_agent = InsightAgent()

    raw_texts = data_agent.run(topic)
    cleaned_texts = cleaner_agent.run(raw_texts)
    sentiments = analyzer_agent.run(cleaned_texts)
    insights = insight_agent.run(sentiments)
    return sentiments, insights
