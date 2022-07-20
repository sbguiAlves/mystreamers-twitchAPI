import requests
import json
import webbrowser

Client_Id = ''
Secret = ''


def get_authorization():
    auth_url = "https://id.twitch.tv/oauth2/authorize"

    aut_params = {
        'response_type': 'code',
        'client_id': Client_Id,
        'redirect_uri': 'http://localhost:3000',
        'scope' : 'user:read:follows'
    }

    request_authorization = requests.get(url=auth_url, params=aut_params)

    webbrowser.register('edge', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"))
    webbrowser.get('edge').open(request_authorization.url)

    ## mandar a requisição, autorizar e pegar o (authorization) code
    ## return code


def get_token(code):
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


def get_id(token, login):
    url = "https://api.twitch.tv/helix/users?login=" + login
    header = get_header(token)

    request = requests.get(url=url, headers=header)
    return request.json()["data"][0]["id"]


def get_header(token):
    head_params = {
        'Authorization': "Bearer " + token,
        'Client-Id': Client_Id
    }
    return head_params


def get_followed_streamers(token, login):
    my_id = get_id(token, login)
    head_url = "https://api.twitch.tv/helix/streams/followed?user_id=" + my_id
    header = get_header(token)

    print("Meu ID: " + my_id)

    request = requests.get(url=head_url, headers=header)
    print(request.json())

    # Parsear do JSON: game_name, type, title, started_at
    # HTML
    # Pensar em uma extensão para navegador


if __name__ == '__main__':
    get_authorization()

    code = input("Insira o código: ")
    token = get_token(code)

    login = input("Insira seu username: ")
    get_followed_streamers(token, login)

