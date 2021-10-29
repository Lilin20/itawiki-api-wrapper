import requests

def login(username, password): # Loggs in into the given account and saves the token in a variable for future usage.
    url = "https://backend.ita-wiki.de/api/auth/login"

    payload = {'email':f'{username}', 'password':f'{password}'}
    headers = {'Accept': 'application/json'}

    response = requests.request("POST", url, headers=headers, params=payload)

    result = response.json()

    global token
    token = result["data"]["token"]
    print(result["message"])

def details(): # Grabs User-Details from the logged in account.
    url = "https://backend.ita-wiki.de/api/auth/user"

    headers = {'Accept': 'application/json' ,"Authorization": f"Bearer {token}"}

    response = requests.request("GET", url, headers=headers)
    return response.json()

def logout():
    url = "https://backend.ita-wiki.de/api/auth/logout"

    headers = {'Accept': 'application/json' ,'Authorization': f'Bearer {token}'}

    response = requests.request("GET", url, headers=headers)
    return response.json()
