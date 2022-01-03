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
    print(createNews(query, result_reddit))
    return result_reddit

def createNews(query:str, data:List[Dict]) -> List[Dict]:
    result = []
    query_serializer = NewsQuerySerializer(data = {'query' : query})
    
    if query_serializer.is_valid():
        query_serializer.save()
        for item in data:
            item.update( {'query':query_serializer.data['id']})
            news_serializer = NewsSerializer(data=item)
            if news_serializer.is_valid():
                news_serializer.save()
                result.append(news_serializer.data)
    
    return result
