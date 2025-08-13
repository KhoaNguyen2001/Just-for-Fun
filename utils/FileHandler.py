import json

class FileHandler:
    @staticmethod
    def readJsonFile(path: str) -> dict:
        with open(path, 'r') as file:
            return json.load(file)