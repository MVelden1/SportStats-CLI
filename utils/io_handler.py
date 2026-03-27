import json


def write_json(file_path, data, indent):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=indent)


def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)
