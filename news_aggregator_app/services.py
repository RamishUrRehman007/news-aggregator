from typing import Dict, List

from rest_framework import serializers

from news_aggregator_app.third_party_integrations import thenews

from .third_party_integrations import (reddit,
    thenews
    )

from .serializers import (NewsSerializer,
    NewsQuerySerializer,
    FavouriteSerializer
    )

from .models import (NewsQuery,
    News,
    Favourite
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

def createFavouriteNews(user:str, id:int) -> List[Dict]:
    try:
        is_favourite = getFavouriteNewsBySearch(user=user, id=id)
        print(is_favourite)
        if is_favourite is None:
            data = {'user':user, 'news':id, 'favourite':True}
            print(data)
            favourite_serializer = FavouriteSerializer(data = data)
            if favourite_serializer.is_valid():
                favourite_serializer.save()
            print(favourite_serializer.data)
            del data['news']
            data.update(getNewsById(id))
            return data
        else:
            is_favourite.update(getNewsById(id))
            return is_favourite
    except:
        return None

def getFavouriteNewsBySearch(user:str, id:int) -> Dict:
    try:
        favourite = Favourite.objects.get(user=user, news=id)
        favourite_serializer = FavouriteSerializer(favourite, many=False)
        favourite_check = True if favourite_serializer.data['favourite'] == False else False
        favourite_check = False if favourite_serializer.data['favourite'] == True else True
        serializer = FavouriteSerializer(instance=favourite, data={'user':user, 'news':id, 'favourite':favourite_check})
        if serializer.is_valid():
            serializer.save()
        return serializer.data
    except:
        return None

def getNewsById(id:int) -> Dict:
    try:
        news = News.objects.get(id=id)
        news_serializer = NewsSerializer(news, many=False)
        return news_serializer.data
    except:
        return None