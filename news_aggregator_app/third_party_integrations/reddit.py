from typing import Dict, List
import requests
import json
from requests.auth import HTTPBasicAuth


def reddit_api(url:str, headers:Dict, params:Dict, query:str = None) -> List[Dict]:
    res = requests.get(url=url, headers=headers, params=params)
    reddit_data = []
    for items in res.json()['data']['children']:
        reddit_data.append({'headline': items['data']['title'], 'link': items['data']['url'], 'source': 'reddit'})
    return reddit_data


def reddit_token(id:str ,key:str, username:str, password:str, headers:Dict) -> Dict:
    url = 'https://www.reddit.com/api/v1/access_token'
    auth = requests.auth.HTTPBasicAuth(id, key)
    data = {'grant_type': 'password', 'username': username, 'password': password}
    response = requests.post(url=url, auth=auth, data=data, headers=headers)
    return response.json()

def reddit(query:str = None) -> List[Dict]:
    # REDDIT
    ID='tLNMiWMoCRhhsvuhtm17FA'
    key='LBBRiuCMHW5Ie81kkn1hXi4KqnNXrQ'
    username = 'ramish534'
    password = 'ramish@rehman'
    reddit_headers = {'User-Agent': 'MyAPI/0.0.1'}
    res = reddit_token(ID,key,username,password,reddit_headers)
    params = {'limit': 30}
    TOKEN = res['access_token']
    reddit_headers['Authorization'] = f'bearer {TOKEN}'

    # if search box is not empty, search the term in the search box else search the whole channel
    search = False
    reddit_data = ''

    if search == True:
        url1=f'https://oauth.reddit.com/r/news/search/?q={query}'
        reddit_data = reddit_api(url1, reddit_headers, params)
        return reddit_data
    else:
        url2='https://oauth.reddit.com/r/news'
        reddit_data = reddit_api(url2, reddit_headers, params)
        return reddit_data
    


