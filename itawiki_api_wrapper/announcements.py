import requests
from itawiki_api_wrapper import auth


def get_announcements():
    url = "https://backend.ita-wiki.de/api/announcements"

    headers = {'Accept': 'application/json' ,"Authorization": f"Bearer {auth.token}"}

    response = requests.request("GET", url, headers=headers)
    result = response.json()

    return result