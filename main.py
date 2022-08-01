import json
from HTMLGenerator import gerador_html
from HttpApiClient import get_authorization, set_access_token, get_followed_streamers
from items import Items

if __name__ == '__main__':
    get_authorization()

    code = input("Insira o código: ")
    access_token = set_access_token(code)

    login = input("Insira seu username: ")
    json_object = get_followed_streamers(access_token, login)

    with open("streams.json", "w") as file:
        json.dump(json_object, file)
        item = Items
        gerador_html(item)

