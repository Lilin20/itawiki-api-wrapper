import requests
from itawiki_api_wrapper import auth


def get_categories():
    url = "https://backend.ita-wiki.de/api/categories/structured"

    headers = {'Accept': 'application/json' ,"Authorization": f"Bearer {auth.token}"}

    response = requests.request("GET", url, headers=headers)
    result = response.json()

    category_list = []
    for i in result['data']:
        category_list.append(i['title'])
    return category_list