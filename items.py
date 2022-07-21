import json
from collections import namedtuple
from datetime import datetime, timedelta


def customDataDecoder(dataDict):
    return namedtuple('X', dataDict.keys())(*dataDict.values())


def verificar_status(status):
    if status == 'live':
        return 'Estamos ao vivo! Vem'
    return 'Estamos offline'


def tempo_transmissao(data_str):
    data_obj = datetime.strptime(data_str, "%Y-%m-%dT%H:%M:%SZ")
    data_inicio = data_obj.strftime("%d/%m, %H:%M:%S")

    hora_atual = datetime.now()
    segundos = (hora_atual - data_obj).seconds

    return f"Começou às: {data_inicio} \u2014 Tempo de Transmissão: {str(timedelta(seconds=segundos))}"


with open('streams.json', encoding="utf-8") as file:
    json_file = file.read()
    data_obj = json.loads(json_file, object_hook=customDataDecoder)


for item in data_obj.data:
    print(item.user_name + " \u2014 Status: " + verificar_status(item.type))
    print("Título: " + item.title)
    print("Jogo atual \u2014 " + item.game_name)
    print(tempo_transmissao(item.started_at) + "\n")

# print(type(data_obj.data[0].user_login))
#print(tempo_transmissao(data_obj.data[0].started_at))
