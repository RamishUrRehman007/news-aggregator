from typing import Dict, List


from news_aggregator_app.third_party_integrations import reddit

def listNews() -> List[Dict]:
    return reddit.reddit()
