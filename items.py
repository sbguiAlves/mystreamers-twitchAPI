import json
from collections import namedtuple
from datetime import datetime, timedelta


class Items:
    def customDataDecoder(dataDict):
        return namedtuple('X', dataDict.keys())(*dataDict.values())


    def tempo_inicio(data_str):
        data_obj = datetime.strptime(data_str, "%Y-%m-%dT%H:%M:%SZ")
        data_atual = datetime.now()
        segundos = (data_atual - data_obj).seconds

        if data_atual.date() == data_obj.date():
            data_inicio = data_obj.strftime("%H:%M")
        else:
            data_inicio = data_obj.strftime("%H:%M (%d/%m)")

        return f"Iniciou às: {data_inicio} <br>Tempo de Transmissão: {str(timedelta(seconds=segundos))}"


    # Main da classe
    with open('streams.json', encoding="utf-8") as file:
        json_file = file.read()
        data_obj = json.loads(json_file, object_hook=customDataDecoder)


    # for item in data_obj.data:
    #     print(item.user_name + " \u2014 Status: " + verificar_status(item.type))
    #     print("Título: " + item.title)
    #     print("Jogo atual \u2014 " + item.game_name)
    #     print(tempo_transmissao(item.started_at) + "\n")

    #print(type(data_obj))
    # print(tempo_transmissao(data_obj.data[0].started_at))