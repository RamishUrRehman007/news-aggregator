from typing import Dict, List

from .third_party_integrations import reddit

def listNews() -> List[Dict]:
    return reddit.reddit()

def searchNews(query:str) -> List[Dict]:
    return reddit.reddit(query=query)
