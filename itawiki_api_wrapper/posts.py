import requests
from itawiki_api_wrapper import auth

def search(keywords):
    unbuild_url = 'https://ita-wiki.de/posts/'

    url = "https://backend.ita-wiki.de/api/search"

    payload = {'keywords':f'{keywords}'}
    headers = {'Accept': 'application/json', "Authorization": f"Bearer {auth.token}"}

    response = requests.request("GET", url, headers=headers, params=payload)

    result = response.json()
    builded_url = unbuild_url + str(result['data']['posts'][0]['id'])
    sorted_results = {'url':builded_url, 'post_id':result['data']['posts'][0]['id'], 'title':result['data']['posts'][0]['title'], 'created_at':result['data']['posts'][0]['created_at']}
    
    return sorted_results