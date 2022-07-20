import json


class Stream:
    def __init__(self, user_name, status, title, game_name, started_at):
        self.user_name = user_name
        self.status = status
        self.title = title
        self.game_name = game_name
        self.started_at = started_at

    def __iter__(self):
        yield from{
            "user_name": self.user_name,
            "status": self.status,
            "title": self.title,
            "game_name": self.game_name,
            "started_at": self.started_at
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


class Data:
    def __init__(self, streams):
        self.streams = streams

    def __iter__(self):
        yield from{
            "data": self.streams
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


with open('streams.json', 'r') as f:
    json_str = f.read()
    json_data = Data(json.loads(json_str))


for item in json_data.streams["data"]:
    print(item["user_name"] + " \u2014 Status: " + item["type"])
    print("Título:" + item["title"])
    print("Jogo atual \u2014 " + item["game_name"])
    print("Data de início: " + item["started_at"] + "\n")

