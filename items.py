import json
from collections import namedtuple
from datetime import datetime, timedelta
from pytz import timezone

class Items:
    def customDataDecoder(dataDict):
        return namedtuple('X', dataDict.keys())(*dataDict.values())

    def data_hora_inicio(self):
        fuso_horario = timezone('America/Sao_Paulo')
        tempo_obj = datetime.strptime(self, "%Y-%m-%dT%H:%M:%S%z")

        tempo_obj_fuso_horario = tempo_obj.astimezone(fuso_horario)
        tempo_str_fuso_horario = tempo_obj_fuso_horario.strftime("%H:%M (%d/%m)")

        return f'<b>Iniciou às:</b> {tempo_str_fuso_horario}'

    def data_hora_transmitido(self):
        tempo_obj = datetime.strptime(self, "%Y-%m-%dT%H:%M:%SZ")

        tempo_atual = datetime.now()
        segundos_obj = (tempo_atual - tempo_obj).seconds
        tempo_transmitido_str = timedelta(seconds=segundos_obj) - timedelta(hours=-3) - timedelta(days=1)

        return f'<b>Transmitindo à:</b> {tempo_transmitido_str}'

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