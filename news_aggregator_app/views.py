from typing import Dict, List
from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .services import listNews

@api_view(['GET'])
def listAndSearchNews(request:Dict) -> List[Dict]:
    query = request.query_params.get('query', None)
    if query is not None:
        # queryset = queryset.filter(category=category)
        listNews(query)
    else:
        listNews()

    return Response(listNews())
