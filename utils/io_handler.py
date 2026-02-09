import json


def write_json(file_path, data, indent):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=indent)


def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
