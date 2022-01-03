from typing import Dict, List

from rest_framework import serializers

from news_aggregator_app.third_party_integrations import thenews

from .third_party_integrations import (reddit,
    thenews
    )

from .serializers import (NewsSerializer,
    NewsQuerySerializer
    )

from .models import (NewsQuery,
    News
    )

import datetime

def listNews() -> List[Dict]:
    return reddit.reddit()

def searchNews(query:str) -> List[Dict]:
    query_id = getQueryByName(query)
    print(query_id)
    if query_id:
        if checkTime(query_id['created_at']) <= 2:
            return getNewsByQuery(query_id['id'])
    
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

def getQueryByName(query:str) -> int:
    try:
        newsquery = NewsQuery.objects.get(query=query)
        serializer = NewsQuerySerializer(newsquery, many=False)
        return serializer.data
    except:
        return None

def getNewsByQuery(query_id:int) -> int:
    news = News.objects.filter(query_id=query_id)
    data_list = []

    for data in news.all():
        data_list.append(
            {
                'link' : data.link,
                'headline' : data.headline,
                'source' : data.source
            }
        )
    return data_list

def checkTime(date):
    today = datetime.datetime.now()
    DD = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    return abs((today - DD).days)