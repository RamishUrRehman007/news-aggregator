from typing import Dict, List

from news_aggregator_app.third_party_integrations import thenews

from .third_party_integrations import (reddit,
    thenews
    )

from .serializers import (NewsSerializer,
    NewsQuerySerializer    
    )

def listNews() -> List[Dict]:
    return reddit.reddit()

def searchNews(query:str) -> List[Dict]:
    result_thenews = thenews.thenews(query=query)
    result_reddit = reddit.reddit(query=query)
    result_reddit.extend(result_thenews)
    print(createNews(query, result_thenews))
    return result_reddit

def createNews(query:str, data:List[Dict]) -> List[Dict]:
    query_serializer = NewsQuerySerializer(data = {'query' : query})
    
    if query_serializer.is_valid():
        query_serializer.save()
    
    return query_serializer.data
