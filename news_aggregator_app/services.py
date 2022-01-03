from typing import Dict, List

from news_aggregator_app.third_party_integrations import thenews

from .third_party_integrations import (reddit,
    thenews
)

def listNews() -> List[Dict]:
    return reddit.reddit()

def searchNews(query:str) -> List[Dict]:
    result_thenews = thenews.thenews(query=query)
    result_reddit = reddit.reddit(query=query)
    result_reddit.extend(result_thenews)
    return result_reddit
