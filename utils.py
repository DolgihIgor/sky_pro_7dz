import json


def load_number_from_json():
    file = open("data.json", "r", encoding="utf-8")
    data = json.load(file)
    file.close()
    return data
