from typing import Dict, List
import requests
import json
from requests.auth import HTTPBasicAuth


def thenews_api(url:str, headers:Dict, query:str) -> List[Dict]:
    res = requests.get(url=url+query, headers=headers)
    thenews_data = []
    for items in res.json()['articles']:
        thenews_data.append({'headline': items['title'], 'link': items['url'], 'source': 'thenews'})
    return thenews_data



def thenews(query) -> List[Dict]:
    # THENEWS
    thenews_headers = {'X-Api-Key': 'e539bb02a8e04179a9bd3c45fac0ef8c'}
    thenews_url = "https://newsapi.org/v2/everything?q="
    thenews_data = thenews_api(thenews_url, thenews_headers, query)
    print(thenews_data)
    


