from typing import Dict, List
from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .services import (listNews,
    searchNews,
    createFavouriteNews,
    getFavouriteNews
)

from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi

@swagger_auto_schema(method='get', manual_parameters=[openapi.Parameter(
    'query', openapi.IN_QUERY, description="Use to search the news", type=openapi.TYPE_STRING
    )], 
    responses = {
    "200": openapi.Response(
        description="Returned the data from Our DB or Third Party Platforms",
        examples={
            "application/json": [{
            "headline": "Tom Holland clarifies his \"If I'm playing Spider-Man at 30, I've done something wrong\" comment",
            "link": "https://v.redd.it/boz1ib8ji6481",
            "source": "reddit",
            "query": 14
        }]
        }
    )
})
@api_view(['GET'])
def listAndSearchNews(request:Dict) -> List[Dict]:
    query = request.query_params.get('query', None)
    if query is not None:
        response_data = searchNews(query)
    else:
        response_data = listNews()

    return Response(response_data)

@swagger_auto_schema(method='get', manual_parameters=[openapi.Parameter(
    'user', openapi.IN_QUERY, description="Name of the user", type=openapi.TYPE_STRING
    )], 
    responses = {
    "200": openapi.Response(
        description="Returned the favourite news data from Our DB",
        examples={
            "application/json": [{
                "user": "hero3",
                "favourite": True,
                "id": 55,
                "link": "/r/teenagers/comments/ff2guk/top_10_biggest_thots_in_history/",
                "headline": "ANGELAA",
                "source": "reddit",
                "created_at": "2022-01-03T18:54:49.235516Z",
                "query": 13
            }]
        }
    )
})
@swagger_auto_schema(method='post', manual_parameters=[openapi.Parameter(
    'user', openapi.IN_QUERY, description="Name of the user", type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
    'id', openapi.IN_QUERY, description="Id of the news, that is stored in our DB, can get from /news?query endpoint", type=openapi.TYPE_STRING
    )], 
    responses = {
    "200": openapi.Response(
        description="Returned the favourite news data from Our DB",
        examples={
            "application/json": [{
            "id": 54,
            "user": "hero3",
            "favourite": False,
            "news": 54,
            "link": "https://i.redd.it/vlaobsmv94b61.jpg",
            "headline": "Sabi Mo Angelaa",
            "source": "reddit",
            "created_at": "2022-01-03T18:54:49.228844Z",
            "query": 13
            }]
        }
    )
})
@api_view(['GET', 'POST'])
def favouriteNews(request:Dict) -> List[Dict]:
    query_user = request.query_params.get('user', None)
    query_id = request.query_params.get('id', None)
     
    if (query_user and query_id) is not None:
        response_data = createFavouriteNews(query_user, query_id)
        if response_data is None:
            return Response({'Message': 'Not Found'}, 404)
    elif query_user is not None:
        response_data = getFavouriteNews(query_user)
        if response_data is None:
            return Response({'Message': 'Not Found'}, 404)
    else:
        response_data = Response({'Message': 'Please provide the query parameters'}, 400)

    return Response(response_data)
