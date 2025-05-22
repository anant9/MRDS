from serpapi import GoogleSearch

def fetch_tweets(topic, limit=10):
    params = {
        "engine": "google",
        "q": f"site:twitter.com {topic}",
        "api_key": "be0aebf8ba07ab8f054fe3ad5dae7cead6e6891c807c7dbdb87dc22cf55ac85a",  # Replace this with your actual SerpAPI key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    tweets = [r['title'] for r in results.get('organic_results', [])[:limit]]
    return tweets