import webbrowser
import requests
import json

Client_Id = ''
Secret = ''

def get_authorization():
    auth_url = "https://id.twitch.tv/oauth2/authorize"

    aut_params = {
        'response_type': 'code',
        'client_id': Client_Id,
        'redirect_uri': 'http://localhost:3000',
        'scope': 'user:read:follows'
    }

    request_authorization = requests.get(url=auth_url, params=aut_params)
    webbrowser.open(request_authorization.url)


def get_access_token(code):
    auth_url = "https://id.twitch.tv/oauth2/token"

    aut_params = {
        'client_id': Client_Id,
        'client_secret': Secret,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:3000'
    }
    request_token = requests.post(url=auth_url, params=aut_params)
    access_token = request_token.json()['access_token']

    return access_token


def get_id(access_token, login):
    url = "https://api.twitch.tv/helix/users?login=" + login
    header = get_header(access_token)

    request = requests.get(url=url, headers=header)
    return request.json()["data"][0]["id"]


def get_header(access_token):
    head_params = {
        'Authorization': "Bearer " + access_token,
        'Client-Id': Client_Id
    }
    return head_params


def get_followed_streamers(access_token, login):

    my_id = get_id(access_token, login)
    head_url = "https://api.twitch.tv/helix/streams/followed?user_id=" + my_id
    header = get_header(access_token)

    request = requests.get(url=head_url, headers=header)

    return request.json()
