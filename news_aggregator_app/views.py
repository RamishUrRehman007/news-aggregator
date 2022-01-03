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
