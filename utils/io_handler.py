import json


def write_json(file_path: str, data: dict, indent: int) -> None:
    with open(file_path, "w") as file:
        json.dump(data, file, indent=indent)


def read_json(file_path: str) -> dict:
    with open(file_path, "r") as file:
        return json.load(file)
