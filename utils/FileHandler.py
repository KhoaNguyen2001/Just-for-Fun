import json
from .IOHandler import IOHandler

class FileHandler:
    @staticmethod
    def readJsonFile(path: str) -> list[dict]:
        try:
            with open(path, 'r') as file:
                return json.load(file)
        except Exception as e:
            IOHandler.printError(f"Error reading JSON file at {path}: {e}")
            return None

    @staticmethod
    def writeJsonFile(path: str, data: dict) -> None:
        try:
            with open(path, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            IOHandler.printError(f"Error writing JSON file at {path}: {e}")