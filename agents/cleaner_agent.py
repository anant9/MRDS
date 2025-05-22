from crewai import Agent
from tools.text_cleaner import clean_and_translate

class CleanerAgent:
    def __init__(self):
        self.agent = Agent(
            name="CleanerAgent",
            role="Cleans and normalizes data",
            goal="Prepare clean, readable input for NLP",
            backstory="You are a data preprocessing expert who excels in cleaning, translating, and normalizing multilingual, noisy, or unstructured text data. Your work ensures that downstream analysis is accurate and reliable."
        )

    def run(self, texts):
        return [clean_and_translate(t) for t in texts]