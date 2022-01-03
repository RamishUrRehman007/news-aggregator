from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def listNews(request):
    api_response = [
        {
        "headline": "Human organs can be stored for three times as long in major breakthrough for transplants",  
        "link": "https://www.telegraph.co.uk/science/2019/09/09/human-organs-can-stored-three-times-long-major-breakthrough/",
        "source": "reddit"
        }
    ]

    return Response(api_response)
