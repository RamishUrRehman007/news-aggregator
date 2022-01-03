from typing import Dict, List
from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .services import (listNews,
    searchNews,
    createFavouriteNews
)

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
    else:
        response_data = ''

    return Response(response_data)
